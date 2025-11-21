#!/usr/bin/env python3
import datetime as dt

from pydantic import AnyUrl

from rembi_mifa import rembi

study = rembi.RembiStudy(
    study=rembi.Study(
        title="the title of my study, which must be quite long",
        description="the title of my study, which must also be quite long",
        private_until_date=dt.date(2025, 11, 21),
        keywords="some, keywords; with|unspecified:delimiters",
        authors=[
            rembi.Author(
                last_name="Bobberton",
                first_name="Alice",
                email="alice.bob@charlie.ac.uk",
                orcid="1111-2222-3333-444X",
                affiliation=rembi.OrganisationUrl(
                    name="Charlietown University",
                    url=AnyUrl("https://charlie.ac.uk"),
                ),
            ),
        ],
    ),
    study_components=[
        rembi.StudyComponent(
            name="my first study component", description="a very helpful description"
        )
    ],
    sample=[
        rembi.Biosample(
            organism=rembi.Organism(
                scientific_name="Drosophila melanogaster",
                ncbi_taxon="https://www.ncbi.nlm.nih.gov/datasets/taxonomy/7215/",
            ),
            biological_entity="fly brains",
        ),
    ],
    specimen=[
        rembi.Specimen(
            sample_preparation="killed fly; sucked out brains",
        )
    ],
    image_acquisition=[
        rembi.ImageAcquisition(
            imaging_method=rembi.ImagingMethod(
                value="bright-field microscopy",
                ontology_name="Biological Imaging Methods Ontology (FBbi)",
                ontology_id="http://purl.obolibrary.org/obo/FBbi_00000243",
            ),
            imaging_instrument="big microscope 1",
            image_acquisition_parameters="flash on",
        )
    ],
)

as_json = study.model_dump_json(indent=2)
print(as_json)

v2 = study.model_validate_json(as_json)
