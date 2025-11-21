from typing import Literal

from pydantic import BaseModel
from .version import REMBI_VERSION


class StudyComponent(BaseModel):
    name: str
    """The name of your study component.

    ## Examples
    - Experiment A
    - Screen B
    - Stitched max-projected fluorescent confocal images
    """

    description: str
    """An explanation of your study component."""

    rembi_version: Literal["1.5"] = REMBI_VERSION  # type:ignore
