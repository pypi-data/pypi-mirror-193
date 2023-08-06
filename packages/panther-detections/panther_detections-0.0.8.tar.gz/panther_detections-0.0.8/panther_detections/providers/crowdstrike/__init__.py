from typing import Literal

from . import queries, rules, sample_logs


def use_all_with_defaults() -> None:
    rules.detection_passthrough()
    rules.dns_request()
    rules.real_time_response_session()
