# sentry_cronjob_monitoring

A small package with a class and a decorator to integrate with Sentrys Cron Monitoring

## Example usage

By class

```python
from sentry_cronjob_monitoring import Monitor
import typer

monitor = Monitor(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    monitor_id="monitor-id-123",
    org_slug="example-org",
)
def main(times: str):
    monitor.checkin()
    sleep_times = times.split(",")
    sleep_time = int(random.choice(sleep_times))
    logger.info(f"will sleep for {sleep_time} seconds")
    sleep(sleep_time)
    logger.info("Done with my sleep")
    monitor.checkout()

if __name__ == "__main__":
    typer.run(main)
```

By decorator

```python
from sentry_cronjob_monitoring import with_monitoring

@with_monitoring(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    monitor_id="monitor-id-123",
    org_slug="example-org",
)
def run():
    logger.info("will sleep for 10 seconds")
    sleep(10)
    logger.info("Done with my sleep")

if __name__ == "__main__":
    run()
```
