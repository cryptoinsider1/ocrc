# ROI Specification v1.0

## Syntax
A ROI MUST conform to the following ABNF:

roi = "roi:" domain "/" type "/" authority "/" timestamp ["/" hash]  
domain = 1*( ALPHA / DIGIT / "-" )  
type = 1*( ALPHA / DIGIT / "-" )  
authority = 1*( ALPHA / DIGIT / "-" / "." )  
timestamp = 8DIGIT ; YYYYMMDD  
hash = 1*( ALPHA / DIGIT )  


- All components are case‑sensitive.
- The hash is optional; if present, it should be a short (6‑12 character) checksum of the object’s content.

## Resolution
ROIs are not automatically resolvable. To resolve an ROI, one may:
- Query a participating registry (see `implementations/`).
- Use search engines or repositories that index ROI metadata.

## Uniqueness
Uniqueness is ensured by the combination of authority, timestamp, and hash. The same logical object may have multiple ROIs if different versions or representations exist.

## Examples

roi:frb/source/chime/20180916/1a2b3c  
roi:frb/event/chime/20200101/4d5e6f  
roi:genomics/sample/ebi/20210315/g7h8i9  
