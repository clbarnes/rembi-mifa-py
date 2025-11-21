from __future__ import annotations
from pydantic import EmailStr, AnyUrl, Field, BaseModel

from ..util import OrcidId


class Author(BaseModel):
    last_name: str
    """Author last name."""

    first_name: str
    """Author first name."""

    email: EmailStr
    """Author email address."""

    orcid: OrcidId | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    """Author ORCID ID."""

    affiliation: OrganisationUrl | OrganisationInfo

    role: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    """Author role in the study."""


class OrganisationUrl(BaseModel):
    """URL to a public registry containing organisation information. ROR recommended"""

    name: str
    """The name of the organisation."""

    url: AnyUrl
    """URL"""


class OrganisationInfo(BaseModel):
    name: str
    """The name of the organisation."""

    address: str
    """The address of the organisation."""
