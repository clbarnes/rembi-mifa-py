#!/usr/bin/env python3
from rembi_mifa import mifa

container = mifa.MifaContainer(
    title="my important study",
    description="'twas a very important study",
    license=mifa.LicenseType.CC_BY,
    funding_statement="the bank of mum and dad",
    annotations=[
        mifa.Annotations(
            annotation_method="hand", annotation_overview="draw things on blackboard"
        )
    ],
)

as_json = container.model_dump_json(indent=2)
print(as_json)
v2 = mifa.MifaContainer.model_validate_json(as_json)
