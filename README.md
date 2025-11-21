# rembi-mifa

Pydantic-based python models for [REMBI](https://www.ebi.ac.uk/bioimage-archive/rembi-model-reference/) and [MIFA](https://www.ebi.ac.uk/bioimage-archive/mifa-model-reference) metadata for [FAIR](https://en.wikipedia.org/wiki/FAIR_data) bioimaging data.

## Usage

### REMBI

```python
from rembi_mifa import rembi

rembi.RembiStudy
```

### MIFA

## Notes

The original specs lack some documentation and have a few other quirks.
The implementation here may differ from the intended structure in these cases.

- The REMBI specification refers to but does not define the `AnnotationType` type;
  here we use the MIFA `AnnotationType` enum.

This implementation is opinionated on certain serialisation/deserialisation features:

- Optional list fields are omitted if empty; optional list fields which are omitted are deserialised to empty lists.
- Date and datetime values are deserialised from RFC 3339 strings or stringified seconds (or milliseconds, depending on the value) since the unix epoch, and serialised to RFC 3339 strings (see the [pydantic docs](https://docs.pydantic.dev/latest/api/standard_library_types/#date-and-time-types) for more details)
- [ORCiD IDs](https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier) may be parsed as only the identifier, but are normalised to URLs; the checksum is also validated
- in a few cases, the specification requires a list but does not state that the list must be non-empty, so this is not validated
- the `keywords` field of `rembi.Study` is probably supposed to represent a delimited list, but it's not specified, so it's left as a plain string here
