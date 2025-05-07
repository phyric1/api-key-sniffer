import json

def load_config(config_path):
    """Loads the configuration file."""
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Failed to load config file: {e}")
        return {}