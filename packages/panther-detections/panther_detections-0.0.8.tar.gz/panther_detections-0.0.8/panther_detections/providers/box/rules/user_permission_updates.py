from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import PERMISSION_UPDATE_EVENT_TYPES, rule_tags


def user_permission_updates(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user has exceeded the threshold for number of folder permission changes within a single time frame."""

    def _title(event: PantherEvent) -> str:
        return (
            f"User [{event.deep_get('created_by', 'login', default='<UNKNOWN_USER>')}]"
            f" exceeded threshold for number of permission changes in the configured time frame."
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Box Large Number of Permission Changes",
        rule_id="Box.Large.Number.Permission.Updates",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityLow,
        description="A user has exceeded the threshold for number of folder "
        "permission changes within a single time frame.",
        tags=rule_tags("Privilege Escalation:Abuse Elevation Control Mechanism"),
        reports={"MITRE ATT&CK": ["TA0004:T1548"]},
        reference="https://developer.box.com/reference/resources/event/",
        runbook="Investigate whether this user's activity is expected.",
        alert_title=_title,
        summary_attrs=["ip_address"],
        threshold=100,
        alert_grouping=detection.AlertGrouping(period_minutes=60),
        filters=[match_filters.deep_in("event_type", PERMISSION_UPDATE_EVENT_TYPES)],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(
                    name="User Permission Change", expect_match=True, data=sample_logs.user_permission_change
                ),
                detection.JSONUnitTest(name="User Shares Item", expect_match=True, data=sample_logs.user_shares_item),
            ]
        ),
    )
