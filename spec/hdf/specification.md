# HDF Specification v1.0

## Overview
The Hypothesis Description Framework (HDF) is a structured way to encode scientific hypotheses, making them machine‑readable and interoperable.

## Core Fields
- `id`: Unique ROI for the hypothesis.
- `title`: Short human‑readable title.
- `description`: Extended explanation.
- `statement`: Formal or natural language statement of the hypothesis.
- `assumptions`: List of underlying assumptions.
- `predictions`: Array of testable predictions, each with an `id`, `description`, and optionally `testable` flag and `requires` (needed observations/methods).
- `falsification_conditions`: Description of what would disprove the hypothesis.
- `related_hypotheses`: Links to other hypotheses with relation type.
- `proposed_by`: Authors (with ORCID or ROI).
- `references`: Bibliographic references.
- `date_proposed`: ISO date.

## Example
See `examples/frb_orbital_hypothesis.json`.
