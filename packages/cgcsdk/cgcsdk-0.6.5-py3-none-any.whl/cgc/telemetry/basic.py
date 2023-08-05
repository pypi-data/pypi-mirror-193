import statsd
import click


def make_statsd_client():
    """Create a statsd client

    :return: statsd client
    :rtype: statsd.StatsClient
    """
    return statsd.StatsClient("77.79.251.163", 8125, prefix="cgc-client")


def increment_metric(metric, is_error: bool = False):
    """Increment a metric

    :param metric: name of metric
    :type metric: str
    """
    if metric is None:
        return
    if is_error:
        metric = f"{metric}.error"
        click.echo(
            f"If you want to open support request, attach command used, status code, error message and information: {metric}"
        )
    else:
        metric = f"{metric}.ok"

    client = make_statsd_client()
    client.incr(metric, 1)


def change_gauge(metric, value):
    """Change a gauge metric

    :param metric: name of metric
    :type metric: str
    :param value: value of metric
    :type value: int
    """
    client = make_statsd_client()
    client.gauge(metric, value, delta=True)


def setup_gauge(metric, value):
    """Setup a gauge metric

    :param metric: name of metric
    :type metric: str
    :param value: value of metric
    :type value: int
    """
    client = make_statsd_client()
    client.gauge(metric, value)
