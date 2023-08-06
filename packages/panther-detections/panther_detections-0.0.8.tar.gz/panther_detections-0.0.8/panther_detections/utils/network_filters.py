from panther_sdk import PantherEvent, detection

__all__ = ["ips_in_cidr"]


def ips_in_cidr(cidr: str, path: str = "p_any_ip_addresses") -> detection.PythonFilter:
    def _ip_in_cidr(obj: PantherEvent) -> bool:
        import collections
        import functools
        import ipaddress

        cidr_network = ipaddress.ip_network(cidr)

        keys = path.split(".")

        obj_at_path = functools.reduce(
            lambda d, key: d.get(key, None) if isinstance(d, collections.abc.Mapping) else None,
            keys,
            obj,
        )

        if obj_at_path is None:
            raise RuntimeError(f"no value found at path '{path}'")

        if isinstance(obj_at_path, str):
            return ipaddress.ip_address(obj_at_path) in cidr_network

        if isinstance(obj_at_path, collections.abc.Iterable):
            for ip_addr in obj_at_path:
                if ipaddress.ip_address(ip_addr) in cidr_network:
                    return True

            return False

        raise RuntimeError(f"IP value at path '{path}' was not a string or iterable")

    return detection.PythonFilter(func=_ip_in_cidr)
