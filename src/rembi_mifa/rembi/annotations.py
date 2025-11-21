from __future__ import annotations
from typing import Annotated
import datetime as dt
from pydantic import BaseModel, Field, model_serializer

from ..util import OmitIfFalsey, omit_falsey
from ..mifa import AnnotationType

from .author import Author


class Annotations(BaseModel):
    """A set of annotations for an AI-ready dataset"""

    authors: Annotated[list[Author], OmitIfFalsey] = Field(default_factory=list)

    file_metadata: Annotated[list[FileLevelMetadata], OmitIfFalsey] = Field(
        default_factory=list
    )

    annotation_overview: str

    annotation_type: Annotated[list[AnnotationType], OmitIfFalsey] = Field(
        default_factory=list
    )
    """N.B. the REMBI specification does not detail the contents of the AnnotationType entity.
    This implementation uses the MIFA AnnotationType.
    """

    annotation_method: str

    annotation_criteria: str | None = None

    annotation_coverage: str | None = None

    annotation_confidence_level: str | None = None

    @model_serializer
    def _serializer(self):
        return omit_falsey(self)


class FileLevelMetadata(BaseModel):
    """Metadata attributes that must be detailed at the file level."""

    annotation_id: str
    annotation_type: Annotated[list[AnnotationType], OmitIfFalsey] = Field(
        default_factory=list
    )
    source_image_id: str
    transformations: str | None = None
    spatial_information: str | None = None
    annotation_creation_time: dt.datetime

    @model_serializer
    def _serializer(self):
        return omit_falsey(self)
