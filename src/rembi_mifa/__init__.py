"""
Implements the REMBI and MIFA metadata specifications for bioimages,
as described by the EBI BioImage Archive: https://www.ebi.ac.uk/bioimage-archive/
"""

from . import rembi
from . import mifa
from importlib.metadata import version as _importlib_metadata_version

__version__ = _importlib_metadata_version("rembi-mifa")


__all__ = ["rembi", "mifa"]
