#!/usr/bin/env python3
"""Minimal RO-Crate validator (checks presence of required fields)."""

import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_rocrate.py <path_to_ro-crate-metadata.json>")
        sys.exit(1)
    metadata_file = Path(sys.argv[1])
    if not metadata_file.exists():
        print("File not found")
        sys.exit(1)

    with open(metadata_file) as f:
        crate = json.load(f)

    # Check basic structure
    if "@context" not in crate:
        print("Missing @context")
        sys.exit(1)
    if "@graph" not in crate:
        print("Missing @graph")
        sys.exit(1)

    # Check for at least one ResearchObject with identifier
    found = False
    for entity in crate["@graph"]:
        if entity.get("@type") == "ResearchObject" and "identifier" in entity:
            found = True
            break
    if not found:
        print("No ResearchObject with identifier found")
        sys.exit(1)

    print("RO-Crate appears valid.")

if __name__ == "__main__":
    main()
