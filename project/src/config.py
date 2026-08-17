import os
from pathlib import Path
from dotenv import load_dotenv

# Absolute path to this file
CONFIG_FILE = Path(__file__).resolve()

# src/
SRC_DIR = CONFIG_FILE.parent

# project/
PROJECT_ROOT = SRC_DIR.parent

# project/.env
load_dotenv(PROJECT_ROOT / ".env")

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

print("CONFIG_FILE:", CONFIG_FILE)
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)
print("RAW_DATA_DIR:", RAW_DATA_DIR)
print("PROCESSED_DATA_DIR:", PROCESSED_DATA_DIR)

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)