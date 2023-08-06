"""Tests for errors."""
import pytest

from use_case_registry.errors import NotDefinedError


@pytest.mark.parametrize(
    argnames=[
        "error",
        "expected_msg",
    ],
    argvalues=[
        (
            ZeroDivisionError(),
            "Something unexpected went wrong. ",
        ),
        (
            Exception("NOT FOUND."),
            "Something unexpected went wrong. NOT FOUND.",
        ),
    ],
)
def test_error_message(error: Exception, expected_msg: str) -> None:
    """Test error message."""
    err = NotDefinedError(error=error)
    assert str(err) == expected_msg
