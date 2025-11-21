import os
import pytest

from pydantic import BaseModel, ValidationError
from pathlib import Path
import runpy

from rembi_mifa.util import OrcidId, orcid_id


TEST_DIR = Path(__file__).parent
PROJECT_DIR = TEST_DIR.parent


class ContainsOrcid(BaseModel):
    orcid: OrcidId


@pytest.mark.parametrize(
    ("in_orcid", "expected"),
    [
        (
            # don't change valid input
            "https://orcid.org/0000-0002-1296-7310",
            "https://orcid.org/0000-0002-1296-7310",
        ),
        (
            # correct HTTP -> HTTPS
            "http://orcid.org/0000-0002-1296-7310",
            "https://orcid.org/0000-0002-1296-7310",
        ),
        (
            # turn into URL
            "0000-0002-1296-7310",
            "https://orcid.org/0000-0002-1296-7310",
        ),
        (
            # accept space-delimited
            "0000 0002 1296 7310",
            "https://orcid.org/0000-0002-1296-7310",
        ),
        (
            # accept un-delimited
            "0000000212967310",
            "https://orcid.org/0000-0002-1296-7310",
        ),
    ],
)
def test_orcid(in_orcid, expected):
    assert orcid_id(in_orcid) == expected
    assert ContainsOrcid.model_validate({"orcid": in_orcid}).orcid == expected


@pytest.mark.parametrize(
    "in_orcid",
    [
        # invalid checksum
        "000000021296731X",
        # unacceptable delimiter
        "0000:0002:1296:7310",
        # some other URL prefix
        "https://isni.org/isni/000000012146438X",
    ],
)
def test_invalid_orcid(in_orcid):
    with pytest.raises(Exception):
        orcid_id(in_orcid)
    with pytest.raises(ValidationError):
        ContainsOrcid.model_validate({"orcid": in_orcid})


@pytest.mark.parametrize(
    "example",
    list((PROJECT_DIR.joinpath("examples").rglob("*.py"))),
    ids=lambda p: p.stem,
)
def test_examples(example):
    runpy.run_path(os.fspath(example))
