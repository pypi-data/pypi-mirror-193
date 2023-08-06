from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import (
    SHARED_SUMMARY_ATTRS,
    create_alert_context,
    rule_tags,
    standard_tags,
)

__all__ = [
    "admin_disabled_mfa",
    "admin_role_assigned",
]


def admin_disabled_mfa(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """An admin user has disabled the MFA requirement for your Okta account"""

    def _title(event: PantherEvent) -> str:
        return f"Okta System-wide MFA Disabled by Admin User {event.udm('actor_user')}"

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Okta MFA Globally Disabled",
        rule_id="Okta.Global.MFA.Disabled",
        log_types=[schema.LogTypeOktaSystemLog],
        tags=rule_tags(
            standard_tags.DATA_MODEL,
            "Defense Evasion:Modify Authentication Process",
        ),
        reports={detection.ReportKeyMITRE: ["TA0005:T1556"]},
        severity=detection.SeverityHigh,
        description="An admin user has disabled the MFA requirement for your Okta account",
        reference="https://developer.okta.com/docs/reference/api/event-types/?q=system.mfa.factor.deactivate",
        runbook="Contact Admin to ensure this was sanctioned activity",
        filters=match_filters.deep_equal("eventType", "system.mfa.factor.deactivate"),
        alert_title=_title,
        alert_context=create_alert_context,
        summary_attrs=SHARED_SUMMARY_ATTRS,
        unit_tests=[
            detection.JSONUnitTest(
                name="MFA Disabled",
                expect_match=True,
                data=sample_logs.system_mfa_factor_deactivate,
            ),
            detection.JSONUnitTest(
                name="Login Event",
                expect_match=False,
                data=sample_logs.user_session_start,
            ),
        ],
    )


def admin_role_assigned(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user has been granted administrative privileges in Okta"""

    def _title(event: PantherEvent) -> str:
        target = event.get("target", [{}])
        display_name = target[0].get("displayName", "MISSING DISPLAY NAME") if target else ""
        alternate_id = target[0].get("alternateId", "MISSING ALTERNATE ID") if target else ""
        privilege = event.deep_get(
            "debugContext",
            "debugData",
            "privilegeGranted",
            default="<UNKNOWN_PRIVILEGE>",
        )

        return (
            f"{event.deep_get('actor', 'displayName')} "
            f"<{event.deep_get('actor', 'alternateId')}> granted "
            f"[{privilege}] privileges to {display_name} <{alternate_id}>"
        )

    def _severity(event: PantherEvent) -> str:
        if event.deep_get("debugContext", "debugData", "privilegeGranted") == "Super administrator":
            return "HIGH"
        return "INFO"

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Okta Admin Role Assigned",
        rule_id="Okta.AdminRoleAssigned",
        log_types=[schema.LogTypeOktaSystemLog],
        tags=rule_tags(
            standard_tags.DATA_MODEL,
            "Privilege Escalation:Valid Accounts",
        ),
        reports={detection.ReportKeyMITRE: ["TA0004:T1078"]},
        severity=detection.DynamicStringField(
            func=_severity,
            fallback=detection.SeverityInfo,
        ),
        description="A user has been granted administrative privileges in Okta",
        reference="https://help.okta.com/en/prod/Content/Topics/Security/administrators-admin-comparison.htm",
        runbook="Reach out to the user if needed to validate the activity",
        filters=[
            match_filters.deep_equal("eventType", "user.account.privilege.grant"),
            match_filters.deep_equal("outcome.result", "SUCCESS"),
            match_filters.deep_equal_pattern("debugContext.debugData.privilegeGranted", r"[aA]dministrator"),
        ],
        alert_title=_title,
        alert_context=create_alert_context,
        summary_attrs=SHARED_SUMMARY_ATTRS,
        unit_tests=[
            detection.JSONUnitTest(
                name="Admin Access Assigned",
                expect_match=True,
                data=sample_logs.admin_access_assigned,
            ),
        ],
    )
