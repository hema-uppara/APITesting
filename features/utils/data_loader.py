import json
import os

def load_json(relative_path: str):
    """
    Load JSON test data from src/data directory
    """
    if not os.path.exists(relative_path):
        raise FileNotFoundError(f"JSON file not found: {relative_path}")

    with open(relative_path, "r", encoding="utf-8") as file:
        return json.load(file)
