from __future__ import annotations
from pydantic import (
    BaseModel,
    Field,
    AnyUrl,
    model_serializer,
)
from typing import Annotated, Literal
import datetime as dt

from .version import REMBI_VERSION

from ..util import IntAsStr, LongStr, OmitIfFalsey, omit_falsey
from .author import Author


class Study(BaseModel):
    """General study information"""

    title: LongStr
    """The title for your dataset.
    This will be displayed when search results including your data are shown.
    Often this will be the same as an associated publication.

    ## Examples
    - Visualization of loop extrusion by DNA nanoscale tracing in single cells
    - SARS-COV-2 drug repurposing - Caco2 cell line
    - Large-scale electron microscopy database for human type 1 diabetes
    """

    description: LongStr
    """Use this field to describe your dataset. This can be the abstract to an accompanying publication."""

    private_until_date: dt.date

    keywords: str
    """Keywords describing your data that can be used to aid search and classification.

    ## Examples
    - RNA localisation
    - CRISPR
    - Brain
    """

    authors: list[Author]

    license: License | None = None

    funding: Funding | None = None

    publications: Annotated[list[Publication], OmitIfFalsey] = Field(
        default_factory=list
    )

    links: Annotated[list[Link], OmitIfFalsey] = Field(default_factory=list)

    rembi_version: Literal["1.5"] = REMBI_VERSION

    @model_serializer
    def _serialize(self):
        return omit_falsey(self)


# class License(BaseModel):
#     """The license under which the data are available."""

License = str


class Funding(BaseModel):
    funding_statement: str
    """A description of how the data generation was funded."""

    grant_references: Annotated[list[GrantReference], OmitIfFalsey] = Field(
        default_factory=list
    )


class GrantReference(BaseModel):
    identifier: str
    """The identifier for the grant."""

    funder: str
    """The funding body providing support."""


class Publication(BaseModel):
    title: str
    """Title of associated publication."""

    authors: str | None = None
    """Authors of associated publication."""

    doi: str | None = None
    """Digital Object Identifier (DOI)."""

    year: IntAsStr | None = None
    """Year of publication."""

    pubmid_id: str | None = None

    @model_serializer
    def _serialize(self):
        return {k: (str(v) if k == "year" and v is not None else v) for k, v in self}


class Link(BaseModel):
    link_url: AnyUrl
    """The URL of a link relevant to the dataset."""

    link_type: str | None = None
    """The type of the link."""

    link_description: str | None = None
    """The description of the linked content.

    ## Examples
    Image analysis code

    Sequencing data

    Project website
    """
