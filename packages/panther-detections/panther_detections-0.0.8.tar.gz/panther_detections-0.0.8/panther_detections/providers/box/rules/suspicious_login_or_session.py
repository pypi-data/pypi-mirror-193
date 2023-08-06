from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils.legacy_utils import deep_get

from .. import sample_logs
from .._shared import SUSPICIOUS_EVENT_TYPES, box_parse_additional_details, rule_tags


def suspicious_login_or_session(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user login event or session event was tagged as medium to high severity by Box Shield."""

    def _title(event: PantherEvent) -> str:
        details = box_parse_additional_details(event)
        description = deep_get(details, "shield_alert", "alert_summary", "description", default="")
        if description:
            return description
        return (
            f"Shield medium to high risk, suspicious event alert triggered for user "
            f"[{deep_get(details, 'shield_alert', 'user', 'email', default='<UNKNOWN_USER>')}]"
        )

    def _filter(event: PantherEvent) -> bool:
        from panther_detections.providers.box._shared import (  # pylint: disable=W0621
            box_parse_additional_details,
        )

        if event.get("event_type") != "SHIELD_ALERT":
            return False
        alert_details = box_parse_additional_details(event).get("shield_alert", {})
        if alert_details.get("rule_category", "") in SUSPICIOUS_EVENT_TYPES:
            if alert_details.get("risk_score", 0) > 50:
                return True
        return False

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Box Shield Suspicious Alert Triggered",
        rule_id="Box.Shield.Suspicious.Alert",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityHigh,
        description="A user login event or session event was tagged as medium to high severity by Box Shield.",
        tags=rule_tags("Initial Access:Valid Accounts"),
        reports={"MITRE ATT&CK": ["TA0001:T1078"]},
        reference="https://developer.box.com/guides/events/shield-alert-events/",
        runbook="Investigate whether this was triggered by an expected user event.",
        alert_title=_title,
        summary_attrs=["event_type", "ip_address"],
        filters=[detection.PythonFilter(func=_filter)],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(
                    name="Suspicious Login Event", expect_match=True, data=sample_logs.suspicious_login_event
                ),
                detection.JSONUnitTest(
                    name="Suspicious Session Event", expect_match=True, data=sample_logs.suspicious_session_event
                ),
                detection.JSONUnitTest(
                    name="Suspicious Session Event - Low Risk",
                    expect_match=False,
                    data=sample_logs.suspicious_session_event___low_risk,
                ),
            ]
        ),
    )
