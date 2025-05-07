import re
import os
import logging
from pathlib import Path
from patterns import ALL_API_KEY_PATTERNS

def extract_match(match):
    """Extracts match value for consistent handling."""
    return match[0] if isinstance(match, (tuple, list)) else match

def should_scan_file(filename, extensions=(".py",)):
    """Checks if a file should be scanned based on its extension."""
    return filename.endswith(extensions)

def scan_file(filepath, patterns):
    """Scans a file for API keys based on given patterns."""
    findings = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            for name, pattern in patterns.items():
                matches = re.findall(pattern, content)
                if matches:
                    findings.append((name, matches))
    except Exception as e:
        print(f"[!] Error reading file {filepath}: {e}")
    return findings

def scan_directory(path, patterns, max_depth):
    """Recursively scans the directory for API keys."""
    print(f"Scanning directory: {path}\n")
    base_depth = len(Path(path).resolve().parts)

    # Check to ensure not going past max depth
    for root, _, files in os.walk(path):
        current_depth = len(Path(root).resolve().parts)
        if current_depth - base_depth >= max_depth:
            continue

        for file in files:
            if should_scan_file(file):
                full_path = os.path.join(root, file)
                results = scan_file(full_path, patterns)

                if results:
                    print(f"\n[!] Potential API Key found in: {full_path}")
                    for name, matches in results:
                        for match in matches:
                            value = extract_match(match)
                            print(f"    - {name}: {value}")
                            logging.info(f"{full_path} - {name}: {value}")