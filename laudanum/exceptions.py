__all__ = ["InvalidRGBAError", "InvalidFontError"]

__doc__ = """
For when ya done goofed.
"""

from typing import Optional


class BaseError(Exception):
    """The mother of all exceptions."""

    def __init__(self, message: Optional[str] = None):
        self.message = "" if message is None else message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


class InvalidRGBAError(BaseError):
    """Raised when you provide an illegal RGBA value."""

    ...


class InvalidFontError(BaseError):
    """Raised when you provide an ASCII font that cannot be found in `art's font gallery <https://www.ascii-art.site/FontList.html>`_."""

    ...
