from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import get_zoom_usergroup_context, rule_tags

__all__ = ["operation_passcode_disabled"]


def operation_passcode_disabled(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """Meeting passcode requirement has been disabled from usergroup"""

    def _title(event: PantherEvent) -> str:
        context = get_zoom_usergroup_context(event)
        return f"Group {context['GroupName']} passcode requirement disabled by {event.get('operator')}"

    def _filter_passcode_disabled(event: PantherEvent) -> bool:
        from panther_detections.providers.zoom._shared import (  # pylint: disable=W0621
            get_zoom_usergroup_context,
        )

        context = get_zoom_usergroup_context(event)
        return "Passcode" in context["Change"] and context["DisabledSetting"]

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Zoom Meeting Passcode Disabled",
        rule_id="Zoom.PasscodeDisabled",
        log_types=schema.LogTypeZoomOperation,
        severity=detection.SeverityLow,
        description="Meeting passcode requirement has been disabled from usergroup",
        tags=rule_tags("Collection:Video Capture"),
        reports={"MITRE ATT&CK": ["TA0009:T1125"]},
        reference="https://support.zoom.us/hc/en-us/articles/360033559832-Zoom-Meeting-and-Webinar-passcodes",
        runbook="Follow up with user or Zoom admin to ensure this meeting room's use case does not allow a passcode.",
        alert_title=_title,
        summary_attrs=["p_any_emails"],
        filters=[
            match_filters.deep_equal("category_type", "User Group"),
            detection.PythonFilter(func=_filter_passcode_disabled),
        ],
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="Meeting Passcode Disabled",
                    expect_match=True,
                    data=sample_logs.operation_passcode_disabled_meeting_passcode_disabled,
                ),
                detection.JSONUnitTest(
                    name="Meeting Passcode Enabled",
                    expect_match=False,
                    data=sample_logs.operation_passcode_disabled_meeting_passcode_enabled,
                ),
            ]
        ),
    )
