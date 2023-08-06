from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import crowdstrike_alert_context, rule_tags

__all__ = ["detection_passthrough"]


def detection_passthrough(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """Crowdstrike Falcon has detected malicious activity on a host."""

    def _title(event: PantherEvent) -> str:
        return f"Crowdstrike Alert ({event.get('Technique')}) - {event.get('ComputerName')}({event.get('UserName')})"

    def _severity(event: PantherEvent) -> str:
        return event.get("SeverityName")

    def _dedup(event: PantherEvent) -> str:
        return f"{event.get('EventUUID')} - {event.get('ComputerName')}"

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Crowdstrike Detection Passthrough",
        rule_id="Crowdstrike.Detection.Passthrough",
        log_types=[
            schema.LogTypeCrowdstrikeFDREvent,
            schema.LogTypeCrowdstrikeDetectionSummary,
        ],
        tags=rule_tags(),
        severity=detection.DynamicStringField(
            func=_severity,
            fallback=detection.SeverityMedium,
        ),
        description="Crowdstrike Falcon has detected malicious activity on a host.",
        runbook="Follow the Falcon console link and follow the IR process as needed.",
        filters=[match_filters.deep_equal("ExternalApiType", "Event_DetectionSummaryEvent")],
        alert_title=_title,
        alert_context=crowdstrike_alert_context,
        summary_attrs=["p_any_ip_addresses"],
        alert_grouping=detection.AlertGrouping(period_minutes=0, group_by=_dedup),
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="Low Severity Finding",
                    expect_match=True,
                    data=sample_logs.low_severity_finding,
                ),
            ]
        ),
    )
