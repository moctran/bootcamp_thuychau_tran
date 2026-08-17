import sys, os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # looks for a .env file in the current and parent directories
print(".env loaded (if present)")

PROJECT_ROOT = Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)

def get_key(name, default=None):
    return os.getenv(name, default)
api_key_present = get_key("API_KEY") is not None
print("API_KEY present:", api_key_present)

data_dir_env = get_key("DATA_DIR", str(DATA_DIR))
data_path = Path(data_dir_env)
# If DATA_DIR from .env is relative, resolve it from PROJECT_ROOT
if not data_path.is_absolute():
    data_path = PROJECT_ROOT / data_path
print("DATA_DIR from env:", data_path)

# Ensure data directory exists (non-destructive)
data_path.mkdir(parents=True, exist_ok=True)
print("Ensured data directory exists.")