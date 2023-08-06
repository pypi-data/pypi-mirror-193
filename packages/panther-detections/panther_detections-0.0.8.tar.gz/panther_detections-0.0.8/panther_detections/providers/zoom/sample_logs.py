import json

user_promoted_to_privileged_role_admin_promotion_event = json.dumps(
    {
        "action": "Batch Update",
        "category_type": "User",
        "operation_detail": "Change Role  - homer.simpson@duff.io: from User to Co-Owner",
        "operator": "admin@duff.io",
        "time": "2022-07-05 20:28:48",
    }
)
user_promoted_to_privileged_role_admin_to_admin = json.dumps(
    {
        "action": "Batch Update",
        "category_type": "User",
        "operation_detail": "Change Role  - homer.simpson@duff.io: from Admin to Co-Owner",
        "operator": "admin@duff.io",
        "time": "2022-07-05 20:28:48",
    }
)
user_promoted_to_privileged_role_admin_to_billing_admin = json.dumps(
    {
        "action": "Batch Update",
        "category_type": "User",
        "operation_detail": "Change Role  - homer.simpson@duff.io: from Admin to Billing Admin",
        "operator": "admin@duff.io",
        "time": "2022-07-05 20:28:48",
    }
)
user_promoted_to_privileged_role_member_to_billing_admin_event = json.dumps(
    {
        "action": "Batch Update",
        "category_type": "User",
        "operation_detail": "Change Role  - homer.simpson@duff.io: from Member to Billing Admin",
        "operator": "admin@duff.io",
        "time": "2022-07-05 20:28:48",
    }
)
user_promoted_to_privileged_role_admin_to_user = json.dumps(
    {
        "action": "Batch Update",
        "category_type": "User",
        "operation_detail": "Change Role  - homer.simpson@duff.io: from Co-Owner to User",
        "operator": "admin@duff.io",
        "time": "2022-07-05 20:28:48",
    }
)
user_promoted_to_privileged_role_coowner_to_admin = json.dumps(
    {
        "action": "Batch Update",
        "category_type": "User",
        "operation_detail": "Change Role  - homer.simpson@duff.io: from Co-Owner to Admin",
        "operator": "admin@duff.io",
        "time": "2022-07-05 20:28:48",
    }
)
user_promoted_to_privileged_role_other_event = json.dumps(
    {
        "action": "SCIM API - Update",
        "category_type": "User",
        "operation_detail": "Edit User homer.simpson@duff.co  - Change Type: from Basic to Licensed",
        "operator": "admin@duff.co",
        "time": "2022-07-01 22:05:22",
    }
)
operation_user_granted_admin_deprecated_user_granted_admin = json.dumps(
    {
        "operator": "homer@panther.io",
        "category_type": "User",
        "action": "Update",
        "operation_detail": "Update User bart@panther.io  - User Role: from Member to Admin",
    }
)
operation_user_granted_admin_deprecated_non_admin_user_update = json.dumps(
    {
        "operator": "homer@panther.io",
        "category_type": "User",
        "action": "Update",
        "operation_detail": "Update User lisa@panther.io  - Job Title: set to Contractor",
    }
)
all_meetings_secured_with_one_option_disabled_turn_off = json.dumps(
    {
        "action": "Update",
        "category_type": "Account",
        "operation_detail": "Security  - Require that all meetings are secured with one security option: from On to Off",  # pylint: disable=C0301
        "operator": "example@example.io",
        "time": "2022-12-16 18:15:38",
    }
)
all_meetings_secured_with_one_option_disabled_turn_on = json.dumps(
    {
        "action": "Update",
        "category_type": "Account",
        "operation_detail": "Security  - Require that all meetings are secured with one security option: from Off to On",  # pylint: disable=C0301
        "operator": "example@example.io",
        "time": "2022-12-16 18:15:38",
    }
)
all_meetings_secured_with_one_option_disabled_non_admin_user_update = json.dumps(
    {
        "action": "Update",
        "category_type": "User",
        "operation_detail": "Update User example@example.io  - Job Title: set to Contractor",
        "operator": "homer@example.io",
    }
)
automatic_sign_out_disabled_automatic_signout_setting_disabled = json.dumps(
    {
        "action": "Update",
        "category_type": "Account",
        "operation_detail": "Security  - Automatically sign users out after a specified time: from On to Off",
        "operator": "example@example.io",
        "time": "2022-12-16 18:20:42",
    }
)
automatic_sign_out_disabled_meeting_setting_disabled = json.dumps(
    {
        "action": "Update",
        "category_type": "Account",
        "operation_detail": "Security  - Require that all meetings are secured with one security option: from On to Off",  # pylint: disable=C0301
        "operator": "example@example.io",
        "time": "2022-12-16 18:15:38",
    }
)
operation_passcode_disabled_meeting_passcode_disabled = json.dumps(
    {
        "time": "2021-11-17 00:37:24Z",
        "operator": "homer@panther.io",
        "category_type": "User Group",
        "action": "Update",
        "operation_detail": "Edit Group Springfield  - Personal Meeting ID (PMI) Passcode: from On to Off",
        "p_log_type": "Zoom.Operation",
    }
)
operation_passcode_disabled_meeting_passcode_enabled = json.dumps(
    {
        "time": "2021-11-17 00:37:24Z",
        "operator": "homer@panther.io",
        "category_type": "User Group",
        "action": "Update",
        "operation_detail": "Edit Group Springfield  - Personal Meeting ID (PMI) Passcode: from Off to On",
        "p_log_type": "Zoom.Operation",
    }
)
