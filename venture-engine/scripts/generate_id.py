#!/usr/bin/env python3
"""Print the next available stable ID; use id_utils.append_record for concurrent writes."""
import argparse
from id_utils import KINDS, next_id

parser = argparse.ArgumentParser()
parser.add_argument("kind", choices=KINDS)
args = parser.parse_args()
print(next_id(args.kind))
