# OCRC RO-Crate Profile v1.0

## Requirements
1. The RO-Crate MUST include a `ResearchObject` entity with an `identifier` property containing the ROI.
2. The `@context` MUST include the OCRC context (`https://ocrc.org/context/v1`).
3. Every entity SHOULD have a `name` and `description`.
4. Provenance (authors, dates) SHOULD be recorded using schema.org properties.

## Example minimal metadata

```json
{
  "@context": ["https://w3id.org/ro/crate/1.1/context", "https://ocrc.org/context/v1"],
  "@graph": [
    {
      "@id": "ro-crate-metadata.json",
      "@type": "CreativeWork",
      "about": {"@id": "./"},
      "conformsTo": {"@id": "https://w3id.org/ro/crate/1.1"}
    },
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "FRB Event 20200101",
      "description": "A single burst from FRB 180916",
      "identifier": "roi:frb/event/chime/20200101/7g8h9i",
      "datePublished": "2020-01-01",
      "author": {"@id": "https://orcid.org/0000-0002-1825-0097"}
    }
  ]
}
```

## Extensions  
Additional domain‑specific types (e.g., FRBEvent, Source) MAY be used by referencing the OCRC ontology.
