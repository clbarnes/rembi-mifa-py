from __future__ import annotations
from pydantic import BaseModel


class Biosample(BaseModel):
    organism: Organism

    biological_entity: str
    """What is being imaged.

    ## Example
    Adult mouse corpus callosum

    Drosophila endoderm

    AC16s human cardiomyocyte cells
    """

    description: str | None = None
    """High level description of the sample

    ## Examples
    - Bronchial epithelial cell culture
    """

    intrinsic_variables: str | None = None
    """Intrinsic (e.g. generic) alteration.

    ## Examples
    - stable overexpression of HIST1H2BJ-mCherry and LMNA
    - Jurkat E6.1 transfected with emerald-VAMP7
    - Homozygous GFP integration into mitotic genes
    """

    extrinsic_variables: str | None = None
    """External treatment (e.g. reagent).

    ## Examples
    - Plate-bound anti-CD3 activation
    - 2-(9-oxoacridin-10-yl)acetic acid
    - cridanimod
    """

    experimental_variables: str | None = None
    """What is intentionally varied between multiple images.

    ## Examples
    - Time
    - Genotype
    - Light exposure
    """


class Organism(BaseModel):
    scientific_name: str
    """Scientific name

    ## Examples
    - Homo sapiens
    - Arabidopsis thaliana
    - Danio rerio
    """

    common_name: str | None = None
    """Common name.

    ## Examples
    - human
    - thale cress
    - zebrafish
    """

    ncbi_taxon: str
    """NCBI Taxon for the organism.

    ## Examples
    - http://purl.obolibrary.org/obo/NCBITaxon_9606
    - http://purl.obolibrary.org/obo/NCBITaxon_3702
    - http://purl.obolibrary.org/obo/NCBITaxon_7955
    """
