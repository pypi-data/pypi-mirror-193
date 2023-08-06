from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import DOMAIN_DENY_LIST, crowdstrike_alert_context, rule_tags

__all__ = ["dns_request"]


def dns_request(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A DNS request was made to a domain on an explicit denylist"""

    def _title(event: PantherEvent) -> str:
        return f"A denylisted domain [{event.get('DomainName')}] was queried by host {event.get('aid')}"

    def _dedup(event: PantherEvent) -> str:
        #  Alert on every individual lookup of a bad domain, per machine
        return f"{event.get('DomainName')}-{event.get('aid')}"

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="DNS request to denylisted domain",
        rule_id="Crowdstrike.DNS.Request",
        enabled=False,
        log_types=[
            schema.LogTypeCrowdstrikeFDREvent,
            schema.LogTypeCrowdstrikeDNSRequest,
        ],
        tags=rule_tags("Initial Access:Phishing"),
        reports={"MITRE ATT&CK": ["TA0001:T1566"]},
        severity=detection.SeverityCritical,
        description="A DNS request was made to a domain on an explicit denylist",
        reference="https://docs.runpanther.io/data-onboarding/supported-logs/crowdstrike#crowdstrike-dnsrequest",
        runbook="Filter for host ID in title in Crowdstrike Host Management console to "
        "identify the system that queried the domain.",
        filters=[match_filters.deep_in("DomainName", DOMAIN_DENY_LIST)],
        alert_title=_title,
        alert_context=crowdstrike_alert_context,
        alert_grouping=detection.AlertGrouping(period_minutes=15, group_by=_dedup),
        summary_attrs=["DomainName", "aid", "p_any_ip_addresses"],
        unit_tests=(
            [
                detection.JSONUnitTest(
                    name="Denylisted Domain",
                    expect_match=True,
                    data=sample_logs.denylisted_domain,
                ),
                detection.JSONUnitTest(
                    name="Non-denylisted Domain",
                    expect_match=False,
                    data=sample_logs.non_denylisted_domain,
                ),
            ]
        ),
    )
