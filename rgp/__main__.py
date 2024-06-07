# type: ignore[attr-defined]
from enum import Enum

import typer
from rich.console import Console

from rgp import version
from rgp.cmd import generate, run_server


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="rgp",
    help="Report generate platform",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]rgp[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def version(
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the rgp package.",
    ),
) -> None:
    """Show version."""


@app.command(name="server")
def generate_report() -> None:
    """Start a preview server."""
    console.print("[bold] Start run report preview server[/]")
    run_server()


@app.command(name="generate")
def generate_report(
    name: str = typer.Option(..., help="Report name to generate."),
) -> None:
    """Generate a report."""
    console.print(f"[bold] Start build report {name}[/]")
    generate(name=name)


if __name__ == "__main__":
    app()
