# Research Object Identifier (ROI)

ROI is a URI scheme for identifying research objects in a decentralized, human‑readable way.

Format:


- `domain` – broad field (e.g., `frb`, `genomics`, `economics`).
- `type` – kind of object (e.g., `source`, `event`, `hypothesis`).
- `authority` – creator or institution (e.g., `chime`, `fast`).
- `timestamp` – date of creation in `YYYYMMDD` format.
- `hash` – short hash of the content (optional, for versioning).

Examples:
- `roi:frb/source/chime/20180916/1a2b3c`
- `roi:frb/event/arecibo/20121102/4d5e6f`

See [specification.md](specification.md) for full details.
