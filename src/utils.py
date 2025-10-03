import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_env(var_name, required=True):
    value = os.environ.get(var_name)
    if required and not value:
        raise ValueError(f"Set {var_name} in your .env")
    return value

def data_path(relative_path: str) -> Path:
    return Path(__file__).parent.parent / "data" / relative_path
