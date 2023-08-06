from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import rule_tags


def user_downloads(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user has exceeded the threshold for number of downloads within a single time frame."""

    def _title(event: PantherEvent) -> str:
        return (
            f"User [{event.deep_get('created_by', 'login', default='<UNKNOWN_USER>')}] "
            f"exceeded threshold for number of downloads in the configured time frame."
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Box Large Number of Downloads",
        rule_id="Box.Large.Number.Downloads",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityLow,
        description="A user has exceeded the threshold for number of downloads within a single time frame.",
        tags=rule_tags("Exfiltration:Exfiltration Over Web Service"),
        reports={"MITRE ATT&CK": ["TA0010:T1567"]},
        reference="https://developer.box.com/reference/resources/event/",
        runbook="Investigate whether this user's download activity is expected. "
        "Investigate the cause of this download activity.",
        alert_title=_title,
        summary_attrs=["ip_address"],
        threshold=100,
        alert_grouping=detection.AlertGrouping(period_minutes=60),
        filters=[match_filters.deep_equal("event_type", "DOWNLOAD")],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(name="User Download", expect_match=True, data=sample_logs.user_download),
            ]
        ),
    )
