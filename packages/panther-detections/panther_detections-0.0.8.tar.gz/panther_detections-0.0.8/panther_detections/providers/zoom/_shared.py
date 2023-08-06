from typing import Any, Dict, List

from panther_sdk import PantherEvent

__all__ = [
    "PRIVILEGED_ROLES",
    "SHARED_TAGS",
    "get_zoom_user_context",
    "get_zoom_usergroup_context",
    "get_zoom_room_context",
    "extract_values",
]

PRIVILEGED_ROLES = ("Admin", "Co-Owner", "Owner", "Billing Admin")

SHARED_TAGS = [
    "Zoom",
]


def rule_tags(*extra_tags: str) -> List[str]:
    return [*SHARED_TAGS, *extra_tags]


def get_zoom_user_context(event: PantherEvent) -> Dict[str, Any]:
    """
    Parses the operation_detail field of Zoom.Operation events related to Users
    to provide usable fields for use in detections
    """
    operation_context = {}
    raw_string = event.get("operation_detail", "")
    category_type = event.get("category_type")
    action = event.get("action")

    if category_type == "User":
        if action in ("Add", "Delete"):
            operation_context["User"] = raw_string.split()[2].strip()
            operation_context["Department"] = raw_string.split("-")[2].split(":")[1].strip()
            operation_context["UserType"] = raw_string.split("-")[1].split(":")[1].strip()

        if action == "Update":
            operation_context["User"] = raw_string.split()[2]
            operation_context["Change"] = " ".join((raw_string.split("-"))).strip()
            operation_context["DisabledSetting"] = "On to Off" in operation_context["Change"]
            operation_context["EnabledSetting"] = "Off to On" in operation_context["Change"]

    return operation_context


def get_zoom_usergroup_context(event: PantherEvent) -> Dict[str, Any]:
    """
    Parses the operation_detail field of Zoom.Operation events related to User Groups
    to provide usable fields for use in detections
    """
    operation_context = {}
    raw_string = event.get("operation_detail", "")
    category_type = event.get("category_type")
    action = event.get("action")

    if category_type == "User Group":
        if action == "Add":
            operation_context["GroupName"] = " ".join(raw_string.split()[2:])

        if action == "Delete":
            operation_context["GroupName"] = " ".join(raw_string.split()[1:])

        if action == "Update":
            operation_context["GroupName"] = " ".join(raw_string.split("-")[0].split()[2:])
            operation_context["Change"] = raw_string.split("-")[1].strip()
            operation_context["DisabledSetting"] = "On to Off" in operation_context["Change"]
            operation_context["EnabledSetting"] = "Off to On" in operation_context["Change"]

    return operation_context


def get_zoom_room_context(event: PantherEvent) -> Dict[str, Any]:
    """
    Parses the operation_detail field of Zoom.Operation events related to Zoom Meeting Rooms
    to provide usable fields for use in detections
    """
    operation_context = {}
    raw_string = event.get("operation_detail", "")
    category_type = event.get("category_type")
    action = event.get("action")

    if category_type == "Zoom Rooms":
        if action == "Update":
            operation_context["Parameter"] = raw_string.split("-")[0]
            operation_context["CurrentState"] = raw_string.split("-")[1].split(":")[1].strip()
            operation_context["PreviousState"] = raw_string.split("-")[2].split(":")[1].strip()
            operation_context["LockStatus"] = raw_string.split("-")[3].split(":")[1].strip()
            operation_context["Affected"] = raw_string.split("-")[4].split(":")[1].strip()

    return operation_context


def extract_values(event):
    import re

    operator = event.get("operator", "<operator-not-found>")
    operation_detail = event.get("operation_detail", "")
    email = re.search(r"[\w.+-c]+@[\w-]+\.[\w.-]+", operation_detail)[0] or "<email-not-found>"
    fromto = re.findall(r"from ([-\s\w]+) to ([-\s\w]+)", operation_detail) or [
        ("<from-role-not-found>", "<to-role-not-found>")
    ]
    from_role, to_role = fromto[0] or ("<role-not-found>", "<role-not-found>")
    return operator, email, from_role, to_role
