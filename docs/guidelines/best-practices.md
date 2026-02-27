# Best Practices for Using OCRC

- **Use persistent identifiers**: Always assign a ROI to every object; reuse existing ROIs when referencing.
- **Include provenance**: In RO-Crate metadata, document who created the data, when, and how.
- **Be explicit in hypotheses**: State falsification conditions clearly; link to predictions.
- **Prefer open formats**: Use JSON, CSV, FITS, etc. Avoid proprietary binaries.
- **Version your objects**: Update ROI with new version suffixes (`roi:.../v2`).
- **Cite related objects**: Use `citation` and `references` fields to link to publications, datasets, and other ROIs.
