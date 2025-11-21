"""
Implements the EBI BioImageArchive MIFA metadata guildeines as specified here:
- https://www.ebi.ac.uk/bioimage-archive/mifa-model-reference/

More details can be found on the website:
- https://www.ebi.ac.uk/bioimage-archive/mifa-overview/
"""

from __future__ import annotations
import sys

if sys.version_info < (3, 11):
    from enum import auto
    from backports.strenum import StrEnum
else:
    from enum import StrEnum, auto
from enum import auto
import datetime as dt
from pydantic import EmailStr, Field, model_serializer, BaseModel

__all__ = [
    "MifaContainer",
    "Publications",
    "Author",
    "OrganisationInfo",
    "GrantReference",
    "LicenseType",
    "Annotations",
    "AnnotationType",
    "FileLevelMetadata",
]


class MifaContainer(BaseModel):
    publications: Publications | None = Field(
        default_factory=lambda x: None, exclude_if=lambda x: x is None
    )
    authors: list[Author] = Field(default_factory=list, exclude_if=lambda x: not x)
    grants: list[GrantReference] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    link_url: list[str] = Field(default_factory=list, exclude_if=lambda x: not x)
    link_description: list[str] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    title: str
    description: str
    keywords: list[str] = Field(default_factory=list, exclude_if=lambda x: not x)
    license: LicenseType
    ai_models_trained: list[str] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    acknowledgements: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    funding_statement: str
    annotations: list[Annotations]


class Publications(BaseModel):
    """Information about any publications associated with the dataset"""

    publication_title: str
    publication_authors: str
    publication_doi: str
    publication_year: int | None = Field(
        default_factory=lambda: None,
        exclude_if=lambda x: x is None,
        coerce_numbers_to_str=True,
    )
    pubmed_id: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )

    @model_serializer
    def _serialize(self):
        return {
            k: (str(v) if k == "publication_year" and v is not None else v)
            for k, v in self
        }


class Author(BaseModel):
    """Information about the authors."""

    organisation: list[OrganisationInfo] = Field(
        default_factory=list, exclude_if=lambda x: len(x) == 0
    )
    author_first_name: str
    author_last_name: str
    email: EmailStr | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    orcid_id: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    role: list[str] = Field(default_factory=list, exclude_if=lambda x: not x)


class OrganisationInfo(BaseModel):
    """Information about the organisation the author is affiliated with."""

    organisation_name: str
    address: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    ror_id: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )


class GrantReference(BaseModel):
    grant_id: str
    funder: str


class LicenseType(StrEnum):
    CC0 = "CC0"
    """No Copyright. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission."""

    CC_BY = "CC_BY"
    """You are free to: Share — copy and redistribute the material in any medium or format. Adapt — remix, transform, and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use."""


class Annotations(BaseModel):
    """A set of annotations for an AI-ready dataset."""

    authors: list[Author] = Field(default_factory=list, exclude_if=lambda x: not x)
    file_metadata: list[FileLevelMetadata] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    annotation_overview: str
    annotation_type: list[AnnotationType] = Field(
        default_factory=list, exclude_if=lambda x: not x
    )
    annotation_method: str
    annotation_criteria: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    annotation_coverage: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    annotation_confidence_level: str | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )


class FileLevelMetadata(BaseModel):
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
    annotation_creation_time: dt.datetime | None = Field(
        None, exclude_if=lambda x: x is None
    )


class AnnotationType(StrEnum):
    CLASS_LABELS = auto()
    """tags that identify specific features, patterns or classes in images"""

    BOUNDING_BOXES = auto()
    """rectangles completely enclosing a structure of interest within an image"""

    COUNTS = auto()
    """number of objects, such as cells, found in an image"""

    DERIVED_ANNOTATIONS = auto()
    """additional analytical data extracted from the images. For example, the image point spread function,the signal to noise ratio, focus information..."""

    GEOMETRICAL_ANNOTATIONS = auto()
    """polygons and shapes that outline a region of interest in the image. These can be geometrical primitives, 2D polygons, 3D meshes"""

    GRAPHS = auto()
    """graphical representations of the morphology, connectivity, or spatial arrangement of biological structures in an image. Graphs, such as skeletons or connectivity diagrams, typically consist of nodes and edges, where nodes represent individual elements or regions and edges represent the connections or interactions between them"""

    POINT_ANNOTATIONS = auto()
    """X, Y, and Z coordinates of a point of interest in an image (for example an object's centroid or landmarks"""

    SEGMENTATION_MASK = auto()
    """an image, the same size as the source image, with the value of each pixel representing some biological identity or background region"""

    TRACKS = auto()
    """annotations marking the movement or trajectory of objects within a sequence of bioimages"""

    WEAK_ANNOTATIONS = auto()
    """rough imprecise annotations that are fast to generate. These annotations are used, for example, to detect an object without providing accurate boundaries"""

    OTHER = auto()
    """other types of annotations, please specify in the annotation overview section"""
