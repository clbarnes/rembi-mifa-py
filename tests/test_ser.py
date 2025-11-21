import datetime as dt
from rembi_mifa.rembi import Specimen, Study


def test_no_null():
    d1 = Specimen(
        sample_preparation="some sample preparation",
        growth_protocol="some growth protocol",
    ).model_dump(mode="json")
    assert "growth_protocol" in d1
    Specimen.model_validate(d1)

    # none by omission
    d2 = Specimen(
        sample_preparation="some sample preparation",
    ).model_dump(mode="json")
    assert "growth_protocol" not in d2
    Specimen.model_validate(d2)

    # explicit none
    d3 = Specimen(
        sample_preparation="some sample preparation",
        growth_protocol=None,
    ).model_dump(mode="json")
    assert "growth_protocol" not in d3
    Specimen.model_validate(d3)


def test_study_no_empty_list():
    s = Study(
        title="t" * 25,
        description="d" * 25,
        private_until_date=dt.date(1, 1, 1),
        keywords="",
        authors=[],
    )
    d = s.model_dump(mode="json")
    assert "authors" in d
    assert "publications" not in d
    assert isinstance(s.publications, list)
    Study.model_validate(d)
