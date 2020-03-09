import click
import uvicorn  # type: ignore

from .. import __version__


@click.group()
def application() -> None:
    """
    .. todo:: Provide application purpose.
    """
    pass


@application.command()
def version() -> None:
    """
    Displays the application version and exists.
    """
    click.echo(__version__)


@application.command()
@click.option("--host", "host", default="127.0.0.1", help="Host to server application from")
@click.option("--port", "port", default=5000, type=int, help="Port to server application from")
@click.option("--log-level", "loglevel", default="info", help="Log level")
def web(host: str, port: str, loglevel: str) -> None:
    """
    Runs the web server.
    """
    uvicorn.run("source.apps.web:App", host=host, port=port, log_level=loglevel)


if __name__ == "__main__":
    application()
