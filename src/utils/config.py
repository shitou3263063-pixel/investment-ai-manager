from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / 'config' / 'settings.yaml'
DATA_DIR = ROOT / 'data'
REPORTS_DIR = ROOT / 'reports'


def load_settings():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
