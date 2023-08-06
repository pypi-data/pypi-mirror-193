from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import rule_tags


def new_login(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user logged in from a new device."""

    def _title(event: PantherEvent) -> str:
        return (
            f"User [{event.deep_get('created_by', 'name', default='<UNKNOWN_USER>')}] " f"logged in from a new device."
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Box New Login",
        rule_id="Box.New.Login",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityInfo,
        description="A user logged in from a new device.",
        tags=rule_tags("Initial Access:Valid Accounts"),
        reports={"MITRE ATT&CK": ["TA0001:T1078"]},
        reference="https://developer.box.com/reference/resources/event/",
        runbook="Investigate whether this is a valid user login.",
        alert_title=_title,
        summary_attrs=["ip_address"],
        filters=[
            # ADD_LOGIN_ACTIVITY_DEVICE
            #  detect when a user logs in from a device not previously seen
            match_filters.deep_equal("event_type", "ADD_LOGIN_ACTIVITY_DEVICE")
        ],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(
                    name="New Login Event", expect_match=True, data=sample_logs.new_login_new_login_event
                ),
            ]
        ),
    )
