from typing import Any, Dict, List

from panther_sdk import PantherEvent

__all__ = [
    "rule_tags",
    "SHARED_TAGS",
    "DOMAIN_DENY_LIST",
    "crowdstrike_alert_context",
]

DOMAIN_DENY_LIST = [
    "baddomain.com",
]

SHARED_TAGS = [
    "Crowdstrike",
]


def rule_tags(*extra_tags: str) -> List[str]:
    return [*SHARED_TAGS, *extra_tags]


def crowdstrike_alert_context(event: PantherEvent) -> Dict[str, Any]:
    """Returns common context for Crowdstrike detections"""

    return {
        "user": event.get("UserName", ""),
        "console-link": event.get("FalconHostLink", ""),
        "commandline": event.get("CommandLine", ""),
        "parentcommandline": event.get("ParentCommandLine", ""),
        "filename": event.get("FileName", ""),
        "filepath": event.get("FilePath", ""),
        "description": event.get("DetectDescription", ""),
        "action": event.get("PatternDispositionDescription", ""),
    }
