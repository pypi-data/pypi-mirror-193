from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import POLICY_VIOLATIONS, rule_tags


def policy_violation(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user violated the content workflow policy."""

    def _title(event: PantherEvent) -> str:
        return (
            f"User [{event.deep_get('created_by', 'name', default='<UNKNOWN_USER>')}] "
            f"violated a content workflow policy."
        )

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Box Content Workflow Policy Violation",
        rule_id="Box.Content.Workflow.Policy.Violation",
        log_types=[schema.LogTypeBoxEvent],
        severity=detection.SeverityLow,
        description="A user violated the content workflow policy.",
        tags=rule_tags(),
        reference="https://developer.box.com/reference/resources/event/",
        runbook="Investigate whether the user continues to violate the policy "
        " and take measure to ensure they understand policy.",
        alert_title=_title,
        summary_attrs=["event_type"],
        filters=[match_filters.deep_in("event_type", POLICY_VIOLATIONS)],
        unit_tests=(
            [
                detection.JSONUnitTest(name="Regular Event", expect_match=False, data=sample_logs.regular_event),
                detection.JSONUnitTest(
                    name="Upload Policy Violation", expect_match=True, data=sample_logs.upload_policy_violation
                ),
                detection.JSONUnitTest(
                    name="Sharing Policy Violation", expect_match=True, data=sample_logs.sharing_policy_violation
                ),
            ]
        ),
    )
