from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils.legacy_utils import deep_get

from .. import sample_logs
from .._shared import box_parse_additional_details, rule_tags


def anomalous_download(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user's download activity has altered significantly."""

    def _title(event: PantherEvent) -> str:
        details = box_parse_additional_details(event)
        description = deep_get(details, "shield_alert", "alert_summary", "description")
        if description:
            return description
        return (
            f"Anomalous download activity triggered by user "
            f"[{deep_get(event, 'created_by', 'name', default='<UNKNOWN_USER>')}]."
        )

    def _filter_rule(event: PantherEvent) -> bool:
        from panther_detections.providers.box._shared import (  # pylint: disable=W0621
            box_parse_additional_details,
        )

        if event.get("event_type") != "SHIELD_ALERT":
            return False
        alert_details = box_parse_additional_details(event).get("shield_alert", {})
        if alert_details.get("rule_category", "") == "Anomalous Download":
            if alert_details.get("risk_score", 0) > 50:
                return True
        return False

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Box Shield Detected Anomalous Download Activity",
        rule_id="Box.Shield.Anomalous.Download",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityHigh,
        description="A user's download activity has altered significantly.",
        tags=rule_tags("Exfiltration:Exfiltration Over Web Service"),
        reports={"MITRE ATT&CK": ["TA0010:T1567"]},
        reference="https://developer.box.com/guides/events/shield-alert-events/",
        runbook="Investigate whether this was triggered by expected user download activity.",
        alert_title=_title,
        summary_attrs=["event_type", "ip_address"],
        filters=[detection.PythonFilter(func=_filter_rule)],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(
                    name="Anomalous Download Event", expect_match=True, data=sample_logs.anomalous_download_event
                ),
            ]
        ),
    )
