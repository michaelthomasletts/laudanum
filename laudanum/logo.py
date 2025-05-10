__all__ = ["Logo"]

__doc__ = """
For creating a logo.
"""

from logging import getLogger
from pathlib import Path
from typing import Tuple

from art import text2art
from attrs import define, field
from attrs.validators import instance_of, optional
from PIL import Image, ImageDraw, ImageFont

from .validators import *

logger = getLogger(__name__)


class LogoParams:
    """Stores default values for the :class:`Logo` object.
    
    Attributes
    ----------
    font : str, optional
        The `ASCII font <https://www.ascii-art.site/FontList.html>`_ that you want to use in your logo. Default is 'alpha'.
    font_size : int, optional
        The size of the text characters that assemble the ASCII image for your logo. Default is 20.
    font_path : str, optional
        The path to the font file for the text characters that assemble the ASCII image for your logo.
    font_color : tuple, optional
        RGBA value for the text characters that assemble the ASCII image for your logo. Default is (255, 0, 0, 255)
    background_color : tuple, optional
        RGBA value for the background color of your logo. Default is (0, 0, 0, 0)
    filename : str, optional
        The location where you want your logo saved. Default matches the `text` parameter plus the ``.pn
    extension : str, optional
        The file extension. Default is '.png'.
    """

    font: str = "alpha"
    font_size: int = 20
    font_color: Tuple[int, int, int, int] = (255, 0, 0, 255)
    background_color: Tuple[int, int, int, int] = (0, 0, 0, 0)
    filename: str = ""
    extension: str = ".png"
    font_path: str = str(
        Path(__file__).parent / "fonts" / "./DejaVuSansMono.ttf"
    )


@define
class Logo:
    """Creates a logo using ASCII art.
    
    Attributes
    ----------
    text : str
        The text to add into your logo.
    font : str, optional
        The `ASCII font <https://www.ascii-art.site/FontList.html>`_ that you want to use in your logo. Default is 'alpha'.
    font_size : int, optional
        The size of the text characters that assemble the ASCII image for your logo. Default is 20.
    font_path : str, optional
        The path to the font file for the text characters that assemble the ASCII image for your logo.
    font_color : tuple, optional
        RGBA value for the text characters that assemble the ASCII image for your logo. Default is (255, 0, 0, 255)
    background_color : tuple, optional
        RGBA value for the background color of your logo. Default is (0, 0, 0, 0)
    filename : str, optional
        The location where you want your logo saved. Default matches the `text` parameter plus the ``.png`` extension.
    
    Methods
    -------
    create()
        Creates the logo.
    
    Notes
    -----
    Only PNG images are permitted in order to support the creation of images with transparent backgrounds via RGBA values.
    The size of images is relative to the size of the rendered ASCII art and cannot be controlled.
    Every font in the `art font gallery <https://www.ascii-art.site/FontList.html>`_ is available.
    The default character font file can be found in the fonts/ submodule of this package.
    
    See Also
    --------
    laudanum.exceptions.InvalidRGBAError
    laudanum.exceptions.InvalidFontError
    
    Examples
    --------
    >>> logo = Logo('howdy')
    >>> logo.create()
    """

    text: str = field(validator=[instance_of(str)])
    font: str = field(
        validator=optional([instance_of(str), validate_font]),
        default=LogoParams.font,
    )
    font_path: str = field(
        validator=optional([instance_of(str)]),
        default=LogoParams.font_path,
    )
    font_size: int = field(validator=optional([instance_of(int)]), default=20)
    font_color: Tuple[int, int, int, int] = field(
        validator=optional([instance_of(tuple), validate_rgba]),
        default=LogoParams.font_color,
    )
    background_color: Tuple[int, int, int, int] = field(
        validator=optional([instance_of(tuple), validate_rgba]),
        default=LogoParams.background_color,
    )
    filename: str = field(
        validator=optional([instance_of(str)]), default=LogoParams.filename
    )
    extension: str = field(init=False)
    extensions: dict = field(init=False)

    def __attrs_post_init__(self):

        self.extension = LogoParams.extension

        if self.filename:
            if "." in self.filename and not self.filename.endswith(
                self.extension
            ):
                logger.warning(f"Filenames must end in '{self.extension}'.")
            else:
                self.filename = self.filename.split(".")[0] + self.extension
        else:
            self.filename = f"{self.text}{self.extension}"

        self.filename = f"{self.text if not self.filename else self.filename.split('.')[0]}{self.extension}"
        self.extensions = Image.registered_extensions()

    def create(self):
        """Creates the ASCII logo.
        
        Raises
        ------
        InvalidRGBAError
            Raised when you provide an illegal RGBA value.
        InvalidFontError
            Raised when you provide a font that cannot be found in art's gallery.
        """

        ascii = text2art(self.text, font=self.font).splitlines()
        _font = ImageFont.truetype(self.font_path, self.font_size)
        bbox = _font.getbbox("A")
        img_width = (bbox[2] - bbox[0]) * max(len(line) for line in ascii)
        img_height = (char_height := bbox[3] - bbox[1]) * len(ascii)
        image = Image.new(
            "RGBA", (img_width, img_height), self.background_color
        )
        draw = ImageDraw.Draw(image)

        for i, line in enumerate(ascii):
            draw.text(
                (0, i * char_height), line, font=_font, fill=self.font_color
            )

        image.save(self.filename, self.extensions[self.extension])

        logger.info(f"Image saved at {self.filename}")
