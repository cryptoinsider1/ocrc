#!/usr/bin/env python3
"""Generate a Research Object Identifier (ROI)."""

import argparse
import hashlib
import sys
from datetime import datetime

def generate_roi(domain, obj_type, authority, content=None):
    timestamp = datetime.now().strftime("%Y%m%d")
    if content:
        hash_digest = hashlib.sha256(content.encode()).hexdigest()[:6]
    else:
        hash_digest = "000000"
    return f"roi:{domain}/{obj_type}/{authority}/{timestamp}/{hash_digest}"

def main():
    parser = argparse.ArgumentParser(description="Generate ROI")
    parser.add_argument("--domain", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--authority", required=True)
    parser.add_argument("--content", help="Content string for hash")
    args = parser.parse_args()
    roi = generate_roi(args.domain, args.type, args.authority, args.content)
    print(roi)

if __name__ == "__main__":
    main()
