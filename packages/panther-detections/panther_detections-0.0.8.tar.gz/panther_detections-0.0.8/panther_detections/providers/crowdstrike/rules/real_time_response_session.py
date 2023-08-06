from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import rule_tags

__all__ = ["real_time_response_session"]


def real_time_response_session(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """Alert when someone uses Crowdstrike’s RTR (real-time response)
    capability to access a machine remotely to run commands."""

    def _title(event: PantherEvent) -> str:

        user_name = event.deep_get("unknown_payload", "UserName", default="<unknown-UserName>")
        hostname_field = event.deep_get("unknown_payload", "HostnameField", default="<unknown-HostNameField>")
        return f"{user_name} started a Crowdstrike Real-Time Response (RTR) shell on {hostname_field}"

    def _alert_context(event: PantherEvent) -> dict:
        return {
            "Start Time": event.deep_get("unknown_payload", "StartTimestamp", default="<unknown-StartTimestamp>"),
            "SessionId": event.deep_get("unknown_payload", "SessionId", default="<unknown-SessionId>"),
            "Actor": event.deep_get("unknown_payload", "UserName", default="<unknown-UserName>"),
            "Target Host": event.deep_get("unknown_payload", "HostnameField", default="<unknown-HostnameField>"),
        }

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Crowdstrike Real Time Response (RTS) Session",
        rule_id="Crowdstrike.RealTimeResponse.Session",
        log_types=[schema.LogTypeCrowdstrikeFDREvent, schema.LogTypeCrowdstrikeUnknown],
        tags=rule_tags(),
        severity=detection.SeverityMedium,
        description="Alert when someone uses Crowdstrike’s RTR (real-time response) capability to access a machine "
        "remotely to run commands.",
        reference="https://falcon.us-2.crowdstrike.com/documentation/71/real-time-response-and-network-containment#"
        "reviewing-real-time-response-audit-logs",
        runbook="Validate the real-time response session started by the Actor.",
        filters=[
            match_filters.deep_equal(
                "unknown_payload.ExternalApiType",
                "Event_RemoteResponseSessionStartEvent",
            )
        ],
        alert_title=_title,
        alert_context=_alert_context,
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="RTS session start event",
                    expect_match=True,
                    data=sample_logs.rts_session_start_event,
                ),
                detection.JSONUnitTest(
                    name="RTS session not started",
                    expect_match=False,
                    data=sample_logs.rts_session_not_started,
                ),
            ]
        ),
    )
