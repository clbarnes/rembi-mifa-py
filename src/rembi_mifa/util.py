import string
from typing import Annotated
from pydantic import AfterValidator
from collections.abc import Iterable, Sequence
import re

ORCID_DIGITS_RE = re.compile(
    r"^(https?://orcid.org/)?(\d\d\d\d[-\s]?\d\d\d\d[-\s]?\d\d\d\d[-\s]?\d\d\d[\dX])$"
)


def len_at_least(min_len: int):
    def validator(s: Sequence):
        assert len(s) > min_len, f"must have length >={min_len}"
        return s

    return validator


LongStr = Annotated[str, AfterValidator(len_at_least(25))]


class OmitIfFalsey:
    pass


def omit_falsey(obj):
    """Use inside a `@model_serializer`.

    ## Examples
    ```python
    @model_serializer
    def _serializer(self):
        return omit_falsey(self)
    ```
    """
    maybe_omit = {
        k
        for k, v in type(obj).model_fields.items()
        if any(isinstance(m, OmitIfFalsey) for m in v.metadata)
    }
    return {k: v for k, v in obj if k not in maybe_omit or not v}


def is_int(s: str) -> int:
    return int(s)


IntAsStr = Annotated[int, AfterValidator(is_int)]


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
