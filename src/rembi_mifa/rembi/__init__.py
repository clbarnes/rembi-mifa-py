"""
Implements REMBI metadata specified here:
- https://www.ebi.ac.uk/bioimage-archive/rembi-model-reference/

More details can be found on the EBI BioImage Archive website:
- https://www.ebi.ac.uk/bioimage-archive/rembi-help-overview/
- https://www.ebi.ac.uk/bioimage-archive/rembi-help-lab/
- https://www.ebi.ac.uk/bioimage-archive/rembi-help-examples/
"""

from __future__ import annotations
from pydantic import AnyUrl, Field, BaseModel

from .annotations import Annotations, FileLevelMetadata, AnnotationType
from .author import Author, OrganisationInfo, OrganisationUrl
from .biosample import Biosample, Organism
from .image_acquisition import ImageAcquisition, ImagingMethod
from .image_analysis import ImageAnalysis
from .image_correlation import ImageCorrelation
from .specimen import Specimen
from .study import Study, License, Link, GrantReference, Funding, Publication
from .study_component import StudyComponent
from .version import REMBI_VERSION


class RembiStudy(BaseModel):
    study: Study
    study_components: list[StudyComponent]
    sample: list[Biosample]
    specimen: list[Specimen]
    image_acquisition: list[ImageAcquisition]
    image_correlation: ImageCorrelation | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    image_analysis: ImageAnalysis | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )
    annotations: Annotations | None = Field(
        default_factory=lambda: None, exclude_if=lambda x: x is None
    )


__all__ = [
    "RembiStudy",
    "REMBI_VERSION",
    "AnyUrl",
    # annotations
    "Annotations",
    "AnnotationType",
    "FileLevelMetadata",
    # author
    "Author",
    "OrganisationInfo",
    "OrganisationUrl",
    # biosample
    "Biosample",
    "Organism",
    # image_acquisition
    "ImageAcquisition",
    "ImagingMethod",
    # image_analysis
    "ImageAnalysis",
    # image_correlation
    "ImageCorrelation",
    # specimen
    "Specimen",
    # study_component
    "StudyComponent",
    # study
    "Study",
    "License",
    "Funding",
    "GrantReference",
    "Publication",
    "Link",
]
