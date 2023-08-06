import typing

from panther_sdk import PantherEvent, detection, schema

from panther_detections.utils import match_filters

from .. import sample_logs
from .._shared import SHARED_SUMMARY_ATTRS, create_alert_context, rule_tags

__all__ = ["geo_improbable_access", "geo_improbable_access_filter"]


# pylint: disable=R0914
def geo_improbable_access_filter() -> detection.PythonFilter:
    def _geo_improbable_access_filter(event: PantherEvent) -> bool:
        from datetime import datetime, timedelta
        from json import dumps, loads
        from math import asin, cos, radians, sin, sqrt

        from panther_oss_helpers import (  # type: ignore
            get_string_set,
            put_string_set,
            set_key_expiration,
        )

        def haversine_distance(grid_one: typing.Any, grid_two: typing.Any) -> float:
            # approximate radius of earth in km
            radius = 6371.0

            # Convert the grid elements to radians
            lon1, lat1, lon2, lat2 = map(
                radians,
                [grid_one["lon"], grid_one["lat"], grid_two["lon"], grid_two["lat"]],
            )

            d_lat = lat2 - lat1
            d_lon = lon2 - lon1

            distance_a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
            distance_c = 2 * asin(sqrt(distance_a))

            return radius * distance_c

        def store_login_info(key: str, old_city: str = "") -> None:
            # Map the user to the lon/lat and time of the most recent login
            put_string_set(
                key,
                [
                    dumps(
                        {
                            "city": event.deep_get("client", "geographicalContext", "city"),
                            "lon": event.deep_get("client", "geographicalContext", "geolocation", "lon"),
                            "lat": event.deep_get("client", "geographicalContext", "geolocation", "lat"),
                            "time": event.get("p_event_time"),
                            "old_city": old_city,
                        }
                    )
                ],
            )
            # Expire the entry after a week so the table doesn't fill up with past users
            set_key_expiration(key, str((datetime.now() + timedelta(days=7)).timestamp()))

        panther_time_format = "%Y-%m-%d %H:%M:%S.%f"
        event_city_tracking = {}

        new_login_stats = {
            "city": event.deep_get("client", "geographicalContext", "city"),
            "lon": event.deep_get("client", "geographicalContext", "geolocation", "lon"),
            "lat": event.deep_get("client", "geographicalContext", "geolocation", "lat"),
        }
        # Bail out if we have a None value in set as it causes false positives
        if None in new_login_stats.values():
            return False

        # Generate a unique cache key for each user
        login_key = f"Okta.Login.GeographicallyImprobable{event.deep_get('actor', 'alternateId')}"
        # Retrieve the prior login info from the cache, if any
        last_login = get_string_set(login_key)
        # If we haven't seen this user login recently, store this login for future use and don't alert
        if not last_login:
            store_login_info(login_key)
            return False
        # Load the last login from the cache into an object we can compare
        old_login_stats = loads(last_login.pop())

        distance = haversine_distance(old_login_stats, new_login_stats)
        old_time = datetime.strptime(old_login_stats["time"][:26], panther_time_format)
        new_time = datetime.strptime(event.get("p_event_time")[:26], panther_time_format)
        time_delta = (new_time - old_time).total_seconds() / 3600  # seconds in an hour

        # Don't let time_delta be 0 (divide by zero error below)
        time_delta = time_delta or 0.0001
        # Calculate speed in Kilometers / Hour
        speed = distance / time_delta

        # Calculation is complete, so store the most recent login for the next check
        store_login_info(login_key, old_city=last_login.get("city", ""))
        event_city_tracking[event.get("p_row_id")] = {
            "new_city": new_login_stats.get("city", "<UNKNOWN_NEW_CITY>"),
            "old_city": old_login_stats.get("city", "<UNKNOWN_OLD_CITY>"),
        }

        return speed > 900  # Boeing 747 cruising speed

    return detection.PythonFilter(func=_geo_improbable_access_filter)


def geo_improbable_access(
    overrides: detection.RuleOverrides = detection.RuleOverrides(),
    extensions: detection.RuleExtensions = detection.RuleExtensions(),
) -> detection.Rule:
    """A user has subsequent logins from two geographic locations that are very far apart"""

    def _title(event: PantherEvent) -> str:
        from panther_oss_helpers import get_string_set  # type: ignore

        login_key = f"Okta.Login.GeographicallyImprobable{event.deep_get('actor', 'alternateId')}"

        # Retrieve the info from the cache, if any
        last_login = get_string_set(login_key)

        # (Optional) Return a string which will be shown as the alert title.
        old_city = last_login.get("old_city", "<NOT_STORED>")
        new_city = last_login.get("city", "<UNKNOWN_NEW_CITY>")

        return (
            f"Geographically improbable login for user [{event.deep_get('actor', 'alternateId')}] "
            f"from [{old_city}]  to [{new_city}]"
        )

    def _group_by(event: PantherEvent) -> str:
        return typing.cast(str, event.deep_get("actor", "alternateId"))

    return detection.Rule(
        overrides=overrides,
        extensions=extensions,
        name="Geographically Improbable Okta Login",
        rule_id="Okta.GeographicallyImprobableAccess",
        log_types=[schema.LogTypeOktaSystemLog],
        tags=rule_tags("Initial Access:Valid Accounts"),
        reports={detection.ReportKeyMITRE: ["TA0001:T1078"]},
        severity=detection.SeverityHigh,
        description="",
        reference="",
        runbook="Reach out to the user if needed to validate the activity, then lock the account",
        filters=[
            match_filters.deep_equal("eventType", "user.session.start"),
            match_filters.deep_equal("outcome.result", "FAILURE"),
            geo_improbable_access_filter(),
        ],
        alert_title=_title,
        alert_context=create_alert_context,
        summary_attrs=SHARED_SUMMARY_ATTRS,
        alert_grouping=detection.AlertGrouping(group_by=_group_by, period_minutes=15),
        unit_tests=[
            detection.JSONUnitTest(
                name="Failed Login",
                expect_match=False,
                data=sample_logs.failed_login,
            ),
        ],
    )
