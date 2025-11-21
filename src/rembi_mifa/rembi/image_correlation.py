from pydantic import BaseModel


class ImageCorrelation(BaseModel):
    """How images from the same correlative study are linked."""

    spatial_and_temporal_alignment: str
    """Method used to correlate images from different modalities.

    ## Examples
    - Manual overlay
    - Alignment algorithm
    """

    fiducials_used: str
    """Features from correlated datasets used for colocalisation."""

    transformations_used: str
    """Correlation transforms."""
