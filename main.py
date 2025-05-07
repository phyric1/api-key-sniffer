import argparse
import os
from config import load_config
from scanner import scan_directory
from logger import setup_logging
from patterns import ALL_API_KEY_PATTERNS

def main():
    # Arguments for running Program
    parser = argparse.ArgumentParser(description="Configurable API Key Scanner (with enabled_patterns)")
    parser.add_argument("directory", help="Directory to scan recursively")
    parser.add_argument("--config", default="config.json", help="Path to config file (default: config.json)")
    args = parser.parse_args()

    # Check if directory is valid
    if not os.path.isdir(args.directory):
        print("[!] Provided path is not a valid directory.")
        return

    # Load config settings
    config = load_config(args.config)
    enabled_names = set(config.get("enabled_patterns", ALL_API_KEY_PATTERNS.keys()))
    max_depth = config.get("max_depth", 5)
    enable_logging = config.get("enable_logging", False)
    log_file = config.get("log_file", "api_key_scan.log")

    setup_logging(enable_logging, log_file)

    # Filter patterns: only include those listed in enabled_patterns
    patterns = {k: v for k, v in ALL_API_KEY_PATTERNS.items() if k in enabled_names}

    scan_directory(args.directory, patterns, max_depth)

if __name__ == "__main__":
    main()