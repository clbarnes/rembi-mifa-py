from __future__ import annotations
import datetime as dt
from pydantic import Field, BaseModel

from ..mifa import AnnotationType

from .author import Author


class Annotations(BaseModel):
    """A set of annotations for an AI-ready dataset"""

    authors: list[Author] = Field(default_factory=list, exclude_if=lambda x: not x)

    file_metadata: list[FileLevelMetadata] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )

    annotation_overview: str

    annotation_type: list[AnnotationType] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    """N.B. the REMBI specification does not detail the contents of the AnnotationType entity.
    This implementation uses the MIFA AnnotationType.
    """

    annotation_method: str

    annotation_criteria: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )

    annotation_coverage: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )

    annotation_confidence_level: str | None = Field(
        None, exclude_if=lambda x: x is None
    )


class FileLevelMetadata(BaseModel):
    """Metadata attributes that must be detailed at the file level."""

    annotation_id: str
    annotation_type: list[AnnotationType] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    source_image_id: str
    transformations: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    spatial_information: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    annotation_creation_time: dt.datetime
