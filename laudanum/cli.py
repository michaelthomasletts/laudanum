__doc__ = """
For the terminal.
"""

from logging import INFO, basicConfig, getLogger
from sys import exit

from click import Tuple, command, option
from rich.console import Console
from rich.logging import RichHandler

from .logo import Logo, LogoParams

console = Console()
basicConfig(
    level=INFO,
    format="%(message)s",
    datefmt=None,
    handlers=[
        RichHandler(
            console=console,
            markup=True,
            rich_tracebacks=True,
            show_path=True,
            enable_link_path=False,
            show_time=False,
        )
    ],
)
logger = getLogger(__name__)

filename_default = "Matches the 'text' parameter by default"


@command()
@option(
    "--text",
    type=str,
    required=True,
    prompt="The text to add to your logo",
    help="The text to add to your logo",
)
@option(
    "--font",
    type=str,
    required=False,
    help="The ASCII font that you want to use in your logo",
    default=LogoParams.font,
)
@option(
    "--fontsize",
    type=int,
    required=False,
    help="The size of the characters that make the ANSII image into your logo",
    default=LogoParams.font_size,
)
@option(
    "--fontcolor",
    type=Tuple([int, int, int, int]),
    required=False,
    help="RGBA value for the font",
    default=LogoParams.font_color,
)
@option(
    "--backgroundcolor",
    type=Tuple([int, int, int, int]),
    required=False,
    help="RGBA for the backgroun",
    default=LogoParams.background_color,
)
@option(
    "--filename",
    type=str,
    required=False,
    help="The filename for the logo image",
    default=filename_default,
)
@option(
    "--fontpath",
    type=str,
    required=False,
    help="The path to the font for assembling your logo",
    default=LogoParams.font_path,
)
def create(
    text: str,
    font: str,
    fontsize: int,
    fontcolor: tuple,
    fontpath: str,
    backgroundcolor: tuple,
    filename: str,
):
    """Creates a logo using ASCII art."""

    if filename == filename_default:
        filename = LogoParams.filename
    try:
        Logo(
            text=text,
            font=font,
            font_size=int(fontsize),
            font_color=fontcolor,
            font_path=fontpath,
            background_color=backgroundcolor,
            filename=filename,
        ).create()
    except Exception as e:
        logger.error(f"[bold red]{type(e).__name__}[/bold red] : {e}")
        exit(1)
