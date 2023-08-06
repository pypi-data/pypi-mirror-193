from panther_sdk import PantherEvent, detection, schema

from panther_detections.providers.okta import sample_logs
from panther_detections.providers.okta._shared import (
    SHARED_SUMMARY_ATTRS,
    create_alert_context,
    rule_tags,
)
from panther_detections.utils import match_filters

__all__ = ["brute_force_logins"]


def brute_force_logins(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user has failed to login more than 5 times in 15 minutes"""

    def _title(event: PantherEvent) -> str:
        return (
            f"Suspected brute force Okta logins to account "
            f"{event.get('actor', {}).get('alternateId', '<UNKNOWN_ACCOUNT>')}, due to "
            f"[{event.get('outcome', {}).get('reason', '<UNKNOWN_REASON>')}]"
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="--DEPRECATED-- Okta Brute Force Logins",
        rule_id="Okta.BruteForceLogins",
        log_types=[schema.LogTypeOktaSystemLog],
        tags=rule_tags(),
        severity=detection.SeverityMedium,
        description="A user has failed to login more than 5 times in 15 minutes",
        reference="https://developer.okta.com/docs/reference/api/system-log/#user-events",
        runbook="Reach out to the user if needed to validate the activity, and then block the IP",
        filters=[
            match_filters.deep_equal("eventType", "user.session.start"),
            match_filters.deep_equal("outcome.result", "FAILURE"),
        ],
        alert_title=_title,
        alert_context=create_alert_context,
        summary_attrs=SHARED_SUMMARY_ATTRS,
        unit_tests=[
            detection.JSONUnitTest(
                name="Failed Login Alert",
                expect_match=True,
                data=sample_logs.failed_login,
            ),
        ],
    )
