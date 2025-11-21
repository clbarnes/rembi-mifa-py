from __future__ import annotations
from pydantic import Field, AnyUrl, BaseModel
from typing import Literal
import datetime as dt

from .version import REMBI_VERSION

from .author import Author


class Study(BaseModel):
    """General study information"""

    title: str = Field(min_length=25)
    """The title for your dataset.
    This will be displayed when search results including your data are shown.
    Often this will be the same as an associated publication.

    ## Examples
    - Visualization of loop extrusion by DNA nanoscale tracing in single cells
    - SARS-COV-2 drug repurposing - Caco2 cell line
    - Large-scale electron microscopy database for human type 1 diabetes
    """

    description: str = Field(min_length=25)
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

    license: License | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )

    funding: Funding | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )

    publications: list[Publication] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )

    links: list[Link] = Field(default_factory=list, exclude_if=lambda x: not x)

    rembi_version: Literal["1.5"] = REMBI_VERSION  # type: ignore


# class License(BaseModel):
#     """The license under which the data are available."""

License = str


class Funding(BaseModel):
    funding_statement: str
    """A description of how the data generation was funded."""

    grant_references: list[GrantReference] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )


class GrantReference(BaseModel):
    identifier: str
    """The identifier for the grant."""

    funder: str
    """The funding body providing support."""


class Publication(BaseModel):
    title: str
    """Title of associated publication."""

    authors: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    """Authors of associated publication."""

    doi: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    """Digital Object Identifier (DOI)."""

    year: int | None = Field(
        default_factory=lambda: None,
        exclude_if=lambda x: x is None,
        coerce_numbers_to_str=True,
    )
    """Year of publication."""

    pubmid_id: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )


class Link(BaseModel):
    link_url: AnyUrl
    """The URL of a link relevant to the dataset."""

    link_type: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    """The type of the link."""

    link_description: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    """The description of the linked content.

    ## Examples
    Image analysis code

    Sequencing data

    Project website
    """
