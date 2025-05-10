__all__ = ["validate_font", "validate_rgba"]

from typing import Tuple, Type

from art import FONT_NAMES
from attrs import Attribute

from .exceptions import *


def validate_font(
    instance: Type["Logo"], attribute: Type[Attribute], value: str
) -> None:
    if value not in FONT_NAMES:
        msg = f"Invalid font selected: '{value}'. Valid options can be found here: https://www.ascii-art.site/FontList.html"
        raise InvalidFontError(msg)


def validate_rgba(
    instance: Type["Logo"],
    attribute: Type[Attribute],
    value: Tuple[int, int, int, int],
):
    if min(value) < 0 or max(value) > 255 or len(value) != 4:
        msg = f"A valid RGBA value must contain three values not exceeding 255 or below 0. You provided '{value}'"
        raise InvalidRGBAError(msg) from None
