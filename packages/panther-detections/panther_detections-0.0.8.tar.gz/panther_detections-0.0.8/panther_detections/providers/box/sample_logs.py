import json

previewed_anonymously = json.dumps(
    {
        "created_by": {"id": "2", "type": "user", "name": "Unknown User"},
        "event_type": "PREVIEW",
        "type": "event",
        "ip_address": "1.2.3.4",
    }
)
suspicious_session_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"shield_alert":{"rule_category":"Suspicious Sessions","risk_score":70,"alert_summary":{"description":"First time in prior month user connected from ip 1.2.3.4."},"user":{"email":"bob@example"}}}',  # pylint: disable=C0301
        "created_by": {"id": "12345678", "type": "user", "login": "bob@example", "name": "Bob Cat"},
        "event_type": "SHIELD_ALERT",
        "source": {"id": "12345678", "type": "user"},
    }
)
missing_created_by = json.dumps({"event_type": "PREVIEW", "type": "event", "ip_address": "1.2.3.4"})
malicious_content = json.dumps(
    {
        "type": "event",
        "additional_details": '{"shield_alert":{"rule_category":"Malicious Content","risk_score":100,"alert_summary":{"upload_activity":{"item_name":"malware.exe"}},"user":{"email":"cat@example"}}}',  # pylint: disable=C0301
        "created_by": {"id": 12345678, "type": "user", "login": "bob@example", "name": "Bob Cat"},
        "event_type": "SHIELD_ALERT",
        "source": {"id": 12345678, "type": "user", "login": "bob@example"},
    }
)
access_granted = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "ACCESS_GRANTED",
        "source": {"id": "12345678", "type": "user", "login": "user@example", "name": "Bob Cat"},
    }
)
regular_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "DELETE",
    }
)
sharing_policy_violation = json.dumps(
    {
        "type": "event",
        "additional_details": {"key": "value"},
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Mountain Lion"},
        "event_type": "CONTENT_WORKFLOW_SHARING_POLICY_VIOLATION",
        "source": {"id": "12345678", "type": "user", "login": "user@example"},
    }
)
regular_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": 12345678, "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "DELETE",
        "source": {
            "item_name": "regular_file.pdf",
            "item_type": "file",
            "owned_by": {"id": 12345678, "type": "user", "login": "cat@example", "name": "Bob Cat"},
            "parent": {"id": 12345, "type": "folder", "etag": 1, "name": "Parent_Folder", "sequence_id": 2},
        },
    }
)
anomalous_download_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"shield_alert":{"rule_category":"Anomalous Download","risk_score":77,"alert_summary":{"description":"Significant increase in download content week over week, 9999% (50.00 MB) more than last week."}}}',  # pylint: disable=C0301
        "created_by": {"id": "12345678", "type": "user", "login": "bob@example", "name": "Bob Cat"},
        "event_type": "SHIELD_ALERT",
        "source": {"id": "12345678", "type": "user", "login": "bob@example", "name": "Bob Cat"},
    }
)
upload_policy_violation = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "CONTENT_WORKFLOW_UPLOAD_POLICY_VIOLATION",
        "source": {"id": "12345678", "type": "user", "login": "user@example"},
    }
)
file_marked_malicious = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "FILE_MARKED_MALICIOUS",
        "source": {
            "item_id": "123456789012",
            "item_name": "bad_file.pdf",
            "item_type": "file",
            "owned_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob"},
            "parent": {"id": "12345", "type": "folder", "etag": "1", "name": "Parent_Folder", "sequence_id": "2"},
        },
    }
)
user_permission_change = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "CHANGE_FOLDER_PERMISSION",
        "source": {"id": "12345678", "type": "user", "login": "user@example", "name": "Bob Cat"},
    }
)
user_shares_item = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "ITEM_SHARED_CREATE",
        "source": {"id": "12345678", "type": "user", "login": "user@example", "name": "Bob Cat"},
    }
)
suspicious_session_event___low_risk = json.dumps(
    {
        "type": "event",
        "additional_details": '{"shield_alert":{"rule_category":"Suspicious Sessions","risk_score":10,"alert_summary":{"description":"First time in prior month user connected from ip 1.2.3.4."},"user":{"email":"bob@example"}}}',  # pylint: disable=C0301
        "created_by": {"id": "12345678", "type": "user", "login": "bob@example", "name": "Bob Cat"},
        "event_type": "SHIELD_ALERT",
        "source": {"id": "12345678", "type": "user"},
    }
)
event_triggered_externally_regular_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example.com", "name": "Bob Cat"},
        "event_type": "DELETE",
    }
)
new_login_new_login_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "ADD_LOGIN_ACTIVITY_DEVICE",
        "source": {"id": "12345678", "type": "user", "login": "user@example"},
    }
)
regular_event = json.dumps(
    {
        "type": "event",
        "additional_details": {'"key": "value"': None},
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "DELETE",
    }
)
login_failed = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "FAILED_LOGIN",
        "source": {"id": "12345678", "type": "user", "name": "Bob Cat"},
    }
)
user_download = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "DOWNLOAD",
        "source": {"id": "12345678", "type": "user", "login": "user@example", "name": "Bob Cat"},
    }
)
regular_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "ceo@example", "name": "Bob Cat"},
        "event_type": "DELETE",
    }
)
suspicious_login_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"shield_alert":{"rule_category":"Suspicious Locations","risk_score":60,"user":{"email":"bob@example"}}}',  # pylint: disable=C0301
        "created_by": {"id": "12345678", "type": "user", "login": "bob@example", "name": "Bob Cat"},
        "event_type": "SHIELD_ALERT",
        "source": {"id": "12345678", "type": "user"},
    }
)
new_login_event = json.dumps(
    {
        "type": "event",
        "additional_details": '{"key": "value"}',
        "created_by": {"id": "12345678", "type": "user", "login": "cat@example", "name": "Bob Cat"},
        "event_type": "DEVICE_TRUST_CHECK_FAILED",
        "source": {"id": "12345678", "type": "user", "login": "user@example"},
    }
)
