from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import PRIVILEGED_ROLES, extract_values, rule_tags

__all__ = ["user_promoted_to_privileged_role"]


def user_promoted_to_privileged_role(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A Zoom user was promoted to a privileged role."""

    def _title(event: PantherEvent) -> str:
        operator, email, from_role, to_role = extract_values(event)
        return f"Zoom: [{email}]'s role was changed from [{from_role}] to [{to_role}] by [{operator}]."

    def _filter(event: PantherEvent) -> bool:
        from panther_detections.providers.zoom._shared import (  # pylint: disable=W0621
            extract_values,
        )

        _, _, from_role, to_role = extract_values(event)
        return to_role in PRIVILEGED_ROLES and from_role not in PRIVILEGED_ROLES

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Zoom User Promoted to Privileged Role",
        rule_id="Zoom.User.Promoted.to.Privileged.Role",
        log_types=schema.LogTypeZoomOperation,
        severity=detection.SeverityMedium,
        tags=rule_tags(),
        description="A Zoom user was promoted to a privileged role.",
        alert_title=_title,
        threshold=1,
        alert_grouping=detection.AlertGrouping(period_minutes=60),
        filters=[
            match_filters.deep_equal_pattern("action", pattern=".+Update"),
            match_filters.deep_equal_pattern("operation_detail", pattern="Change Role.+"),
            match_filters.deep_equal("category_type", "User"),
            detection.PythonFilter(func=_filter),
        ],
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="Admin Promotion Event",
                    expect_match=True,
                    data=sample_logs.user_promoted_to_privileged_role_admin_promotion_event,
                ),
                detection.JSONUnitTest(
                    name="Admin to Admin",
                    expect_match=False,
                    data=sample_logs.user_promoted_to_privileged_role_admin_to_admin,
                ),
                detection.JSONUnitTest(
                    name="Admin to Billing Admin",
                    expect_match=False,
                    data=sample_logs.user_promoted_to_privileged_role_admin_to_billing_admin,
                ),
                detection.JSONUnitTest(
                    name="Member to Billing Admin Event",
                    expect_match=True,
                    data=sample_logs.user_promoted_to_privileged_role_member_to_billing_admin_event,
                ),
                detection.JSONUnitTest(
                    name="Admin to User",
                    expect_match=False,
                    data=sample_logs.user_promoted_to_privileged_role_admin_to_user,
                ),
                detection.JSONUnitTest(
                    name="CoOwner to Admin",
                    expect_match=False,
                    data=sample_logs.user_promoted_to_privileged_role_coowner_to_admin,
                ),
                detection.JSONUnitTest(
                    name="Other Event",
                    expect_match=False,
                    data=sample_logs.user_promoted_to_privileged_role_other_event,
                ),
            ]
        ),
    )
