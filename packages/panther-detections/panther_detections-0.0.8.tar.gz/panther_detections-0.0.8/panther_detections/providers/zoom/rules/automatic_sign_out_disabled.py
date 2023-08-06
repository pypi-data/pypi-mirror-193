from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import rule_tags

__all__ = ["automatic_sign_out_disabled"]


def automatic_sign_out_disabled(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A Zoom User turned off your organization's setting to automatically
    sign users out after a specified period of time."""

    def _title(event: PantherEvent) -> str:
        return (
            f"Zoom User [{event.get('operator', '<NO_OPERATOR>')}] turned off your organization's "
            f"setting to automatically sign users out after a specified time."
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Zoom Automatic Sign Out Disabled",
        rule_id="Zoom.Automatic.Sign.Out.Disabled",
        log_types=schema.LogTypeZoomOperation,
        severity=detection.SeverityMedium,
        tags=rule_tags(),
        description="A Zoom User turned off your organization's setting to automatically sign users out "
        "after a specified period of time.",
        reference="https://support.zoom.us/hc/en-us/articles/115005756143-Changing-account-security-settings#:~:text=Users%20need%20to%20sign%20in,of%205%20to%20120%20minutes",  # pylint: disable=C0301
        runbook="Confirm this user acted with valid business intent and determine whether this activity "
        "was authorized.",
        alert_title=_title,
        threshold=1,
        alert_grouping=detection.AlertGrouping(period_minutes=60),
        filters=[
            match_filters.deep_equal("action", "Update"),
            match_filters.deep_equal("category_type", "Account"),
            match_filters.deep_equal_pattern(
                "operation_detail", ".+Automatically sign users out after a specified time: from On to Off"
            ),
        ],
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="Automatic Signout Setting Disabled",
                    expect_match=True,
                    data=sample_logs.automatic_sign_out_disabled_automatic_signout_setting_disabled,
                ),
                detection.JSONUnitTest(
                    name="Meeting Setting Disabled",
                    expect_match=False,
                    data=sample_logs.automatic_sign_out_disabled_meeting_setting_disabled,
                ),
            ]
        ),
    )
