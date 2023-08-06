"""Custom defined errors."""


class CommandInputValidationError(Exception):
    """Raised when command input values does pass validation check."""


class NotDefinedError(Exception):
    """Not defined error placeholder."""

    def __init__(self, error: Exception) -> None:
        """Construct class."""
        super().__init__(f"Something unexpected went wrong. {error}")
