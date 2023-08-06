from typing import Any, Dict, List

from panther_sdk import PantherEvent

from panther_detections.utils import standard_tags

__all__ = [
    "rule_tags",
    "SUPPORT_ACCESS_EVENTS",
    "SUPPORT_RESET_EVENTS",
    "SHARED_TAGS",
    "SHARED_SUMMARY_ATTRS",
    "create_alert_context",
]

SUPPORT_ACCESS_EVENTS = [
    "user.session.impersonation.grant",
    "user.session.impersonation.initiate",
]

SUPPORT_RESET_EVENTS = [
    "user.account.reset_password",
    "user.mfa.factor.update",
    "system.mfa.factor.deactivate",
    "user.mfa.attempt_bypass",
]

SHARED_TAGS = [
    "Okta",
    standard_tags.IDENTITY_AND_ACCESS_MGMT,
]

SHARED_SUMMARY_ATTRS = [
    "eventType",
    "severity",
    "displayMessage",
    "p_any_ip_addresses",
]


def rule_tags(*extra_tags: str) -> List[str]:
    return [*SHARED_TAGS, *extra_tags]


def create_alert_context(event: PantherEvent) -> Dict[str, Any]:
    """Returns common context for Okta alerts"""

    return {
        "ips": event.get("p_any_ip_addresses", []),
        "actor": event.get("actor", ""),
        "target": event.get("target", ""),
        "client": event.get("client", ""),
    }
