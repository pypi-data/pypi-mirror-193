from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils.legacy_utils import deep_get

from .. import sample_logs
from .._shared import box_parse_additional_details, rule_tags


def malicious_content(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """Box has detect malicious content, such as a virus."""

    def _title(event: PantherEvent) -> str:
        if event.get("event_type") == "FILE_MARKED_MALICIOUS":
            return (
                f"File [{deep_get(event, 'source', 'item_name', default='<UNKNOWN_FILE>')}], owned by "
                f"[{deep_get(event, 'source', 'owned_by', 'login', default='<UNKNOWN_USER>')}], "
                f"was marked malicious."
            )
        alert_details = box_parse_additional_details(event).get("shield_alert", {})
        return (
            f"File [{deep_get(alert_details, 'user', 'email', default='<UNKNOWN_USER>')}], owned by "
            f"[{deep_get(alert_details, 'alert_summary', 'upload_activity', 'item_name', default='<UNKNOWN_FILE>')}], "
            f"was marked malicious."
        )

    def _filter_malicious_file(event: PantherEvent) -> bool:
        from panther_detections.providers.box._shared import (  # pylint: disable=W0621
            box_parse_additional_details,
        )

        # enterprise  malicious file alert event
        if event.get("event_type") == "FILE_MARKED_MALICIOUS":
            return True
        # Box Shield will also alert on malicious content
        if event.get("event_type") != "SHIELD_ALERT":
            return False
        alert_details = box_parse_additional_details(event).get("shield_alert", {})
        if alert_details.get("rule_category", "") == "Malicious Content":
            if alert_details.get("risk_score", 0) > 50:
                return True
        return False

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Malicious Content Detected",
        rule_id="Box.Malicious.Content",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityHigh,
        description="Box has detect malicious content, such as a virus.",
        tags=rule_tags("Execution:User Execution"),
        reports={"MITRE ATT&CK": ["TA0002:T1204"]},
        reference="https://developer.box.com/guides/events/shield-alert-events/,  https://developer.box.com/reference/resources/event/",  # pylint: disable=C0301
        runbook="Investigate whether this is a false positive or if the virus needs to be contained appropriately.",
        alert_title=_title,
        summary_attrs=["event_type"],
        filters=[detection.PythonFilter(_filter_malicious_file)],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(
                    name="File marked malicious", expect_match=True, data=sample_logs.file_marked_malicious
                ),
                detection.JSONUnitTest(name="Malicious Content", expect_match=True, data=sample_logs.malicious_content),
            ]
        ),
    )
