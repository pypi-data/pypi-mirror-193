from typing import List, Literal, Union

from panther_sdk import detection

from . import rules, sample_logs
from ._shared import *


def use_all_with_defaults() -> List[Union[detection.Rule]]:
    return [
        rules.access_granted(),
        rules.anomalous_download(),
        rules.malicious_content(),
        rules.new_login(),
        rules.policy_violation(),
        rules.suspicious_login_or_session(),
        rules.untrusted_device(),
        rules.user_downloads(),
        rules.user_permission_updates(),
    ]
