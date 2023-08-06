from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import rule_tags

__all__ = ["all_meetings_secured_with_one_option_disabled"]


def all_meetings_secured_with_one_option_disabled(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A Zoom User turned off your organization's requirement that all meetings are secured with one security option."""

    def _title(event: PantherEvent) -> str:
        return (
            f"Zoom User [{event.get('operator', '<NO_OPERATOR>')}] turned off your organization's "
            f"requirement to secure all meetings with one security option."
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Zoom All Meetings Secured With One Option Disabled",
        rule_id="Zoom.All.Meetings.Secured.With.One.Option.Disabled",
        log_types=schema.LogTypeZoomOperation,
        severity=detection.SeverityMedium,
        tags=rule_tags(),
        description="A Zoom User turned off your organization's requirement that all meetings"
        " are secured with one security option.",
        runbook="Confirm this user acted with valid business intent and determine whether this"
        " activity was authorized.",
        alert_title=_title,
        threshold=1,
        alert_grouping=detection.AlertGrouping(period_minutes=60),
        filters=[
            match_filters.deep_equal("action", "Update"),
            match_filters.deep_equal("category_type", "Account"),
            match_filters.deep_equal_pattern(
                "operation_detail", ".+Require that all meetings are secured with one security option: from On to Off"
            ),
        ],
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="Turn off",
                    expect_match=True,
                    data=sample_logs.all_meetings_secured_with_one_option_disabled_turn_off,
                ),
                detection.JSONUnitTest(
                    name="Turn on",
                    expect_match=False,
                    data=sample_logs.all_meetings_secured_with_one_option_disabled_turn_on,
                ),
                detection.JSONUnitTest(
                    name="Non admin user update",
                    expect_match=False,
                    data=sample_logs.all_meetings_secured_with_one_option_disabled_non_admin_user_update,
                ),
            ]
        ),
    )
