#!/usr/bin/env python3
"""Module for converting CSV to JSON."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON format and save to data.json."""
    try:
        with open(csv_filename) as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w") as f:
            json.dump(data, f)
        return True
    except Exception:
        return False
