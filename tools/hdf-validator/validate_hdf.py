#!/usr/bin/env python3
"""Validate an HDF JSON file against the schema."""

import json
import sys
import jsonschema
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_hdf.py <hdf_file> [schema_file]")
        sys.exit(1)
    hdf_file = sys.argv[1]
    schema_file = sys.argv[2] if len(sys.argv) > 2 else Path(__file__).parent / "../../spec/hdf/schema/hypothesis_schema.json"

    with open(hdf_file) as f:
        instance = json.load(f)
    with open(schema_file) as f:
        schema = json.load(f)

    try:
        jsonschema.validate(instance, schema)
        print("HDF file is valid.")
    except jsonschema.ValidationError as e:
        print("Validation error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
