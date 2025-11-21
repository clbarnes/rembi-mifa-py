import string
from typing import Annotated
from pydantic import AfterValidator, Field
from collections.abc import Iterable
import re

ORCID_DIGITS_RE = re.compile(
    r"^(https?://orcid.org/)?(\d\d\d\d[-\s]?\d\d\d\d[-\s]?\d\d\d\d[-\s]?\d\d\d[\dX])$"
)


def iso_7064_11_2(s: str) -> Iterable[str]:
    """Yield the digits of an ISO-7604 mod11-2 string.

    Raises an AssertionError if the checksum is invalid.

    https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
    """
    total = 0
    for c in s[:-1]:
        if c not in string.digits:
            continue
        yield c
        total = (total + int(c)) * 2
    remainder = total % 11
    result = (12 - remainder) % 11
    chk = s[-1]
    if result == 10:
        assert chk == "X", "Invalid checksum"
    else:
        assert result == int(chk), "Invalid checksum"
    yield chk


def orcid_id(s: str) -> str:
    """
    - Ensure that the ORCiD is a URL
    - Correct HTTP to HTTPS
    - Ensure correct formatting of the digit groups
    - Validate the checksum
    """
    digits = ORCID_DIGITS_RE.search(s)
    assert digits is not None, f"Could not find ORCiD digits in string {s}"

    out_chars = []
    for idx, digit in enumerate(iso_7064_11_2(digits.group(2))):
        if idx and idx % 4 == 0:
            out_chars.append("-")
        out_chars.append(digit)

    return "https://orcid.org/" + "".join(out_chars)


OrcidId = Annotated[str, AfterValidator(orcid_id)]


def maybe():
    return Field(default_factory=lambda: None, exclude_if=lambda x: x is None)


def maybe_list():
    return Field(default_factory=list, exclude_if=lambda x: len(x) == 0)
