from typing import Any, Callable

import httpx


class Monitor:
    def __init__(self, dsn: str, monitor_id: str, org_slug: str) -> None:
        """
        Args:
            dsn (str): DSN for project with current Cronjob
            monitor_id (str): ID for your monitor in sentry.
            org_slug (str): Your sentry organization's slug

        For more infomation see sentry official documentation: https://docs.sentry.io/product/crons/
        """
        self._client = httpx.Client()
        self._client.headers.update({"Authorization": f"DSN {dsn}"})
        self.dsn = dsn
        self.monitor_id = monitor_id
        self.org_slug = org_slug

    def checkin(self):
        url = f"https://sentry.io/api/0/organizations/{self.org_slug}/monitors/{self.monitor_id}/checkins/"
        response = self._client.post(url=url, json={"status": "in_progress"})
        self.checkin_id = response.json()["id"]

    def checkout(self):
        url = f"https://sentry.io/api/0/organizations/{self.org_slug}/monitors/{self.monitor_id}/checkins/{self.checkin_id}/"
        self._client.put(url=url, json={"status": "ok"})
        self._client.close()


def with_monitoring(dsn: str, monitor_id: str, org_slug: str):
    """
    Args:
        dsn (str): DSN for project with current Cronjob
        monitor_id (str): ID for your monitor in sentry.
        org_slug (str): Your sentry organization's slug

    For more infomation see sentry official documentation: https://docs.sentry.io/product/crons/
    """
    monitor = Monitor(dsn=dsn, monitor_id=monitor_id, org_slug=org_slug)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            monitor.checkin()
            results = func(*args, **kwargs)
            monitor.checkout()
            return results

        return wrapper

    return decorator
