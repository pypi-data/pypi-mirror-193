from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import (
    SHARED_SUMMARY_ATTRS,
    SUPPORT_ACCESS_EVENTS,
    SUPPORT_RESET_EVENTS,
    create_alert_context,
    rule_tags,
    standard_tags,
)

__all__ = [
    "account_support_access",
    "support_reset",
]


def account_support_access(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """Detects when an admin user has granted access to Okta Support for your account"""

    def _title(event: PantherEvent) -> str:
        return f"Okta Support Access Granted by {event.udm('actor_user')}"

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Okta Support Access Granted",
        rule_id="Okta.Support.Access",
        log_types=[schema.LogTypeOktaSystemLog],
        tags=rule_tags(standard_tags.DATA_MODEL, "Initial Access:Trusted Relationship"),
        reports={detection.ReportKeyMITRE: ["TA0001:T1199"]},
        severity=detection.SeverityMedium,
        description="An admin user has granted access to Okta Support to your account",
        reference="https://help.okta.com/en/prod/Content/Topics/Settings/settings-support-access.htm",
        runbook="Contact Admin to ensure this was sanctioned activity",
        filters=[
            match_filters.deep_in("eventType", SUPPORT_ACCESS_EVENTS),
        ],
        alert_title=_title,
        alert_context=create_alert_context,
        summary_attrs=SHARED_SUMMARY_ATTRS,
        unit_tests=[
            detection.JSONUnitTest(
                name="Support Access Granted",
                expect_match=True,
                data=sample_logs.user_session_impersonation_grant,
            ),
            detection.JSONUnitTest(
                name="Login Event",
                expect_match=False,
                data=sample_logs.user_session_start,
            ),
        ],
    )


def support_reset(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A Password or MFA factor was reset by Okta Support"""

    def _title(event: PantherEvent) -> str:
        return f"Okta Support Reset Password or MFA for user {event.udm('actor_user')}"

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Okta Support Reset Credential",
        rule_id="Okta.Support.Reset",
        log_types=[schema.LogTypeOktaSystemLog],
        tags=rule_tags(standard_tags.DATA_MODEL, "Initial Access:Trusted Relationship"),
        reports={detection.ReportKeyMITRE: ["TA0001:T1199"]},
        severity=detection.SeverityHigh,
        description="A Password or MFA factor was reset by Okta Support",
        reference="https://help.okta.com/en/prod/Content/Topics/Directory/get-support.htm#"
        ":~:text=Visit%20the%20Okta%20Help%20Center,1%2D800%2D219%2D0964",
        runbook="Contact Admin to ensure this was sanctioned activity",
        filters=[
            match_filters.deep_in("eventType", SUPPORT_RESET_EVENTS),
            match_filters.deep_equal("actor.alternateId", "system@okta.com"),
            match_filters.deep_equal("transaction.id", "unknown"),
            match_filters.deep_equal("userAgent.rawUserAgent", None),
            match_filters.deep_equal("client.geographicalContext.country", None),
        ],
        alert_title=_title,
        alert_context=create_alert_context,
        summary_attrs=SHARED_SUMMARY_ATTRS,
        unit_tests=[
            detection.JSONUnitTest(
                name="Support Reset Credential",
                expect_match=True,
                data=sample_logs.support_password_reset,
            ),
            detection.JSONUnitTest(
                name="Reset by Company Admin",
                expect_match=False,
                data=sample_logs.admin_password_reset,
            ),
        ],
    )
