# API Key Sniffer

A Python script to scan for API keys and sensitive tokens within files or directories. It uses regular expressions to search for a variety of API key formats and other keywords.

## Installation

### Clone the repository:
```bash
git clone https://github.com/phyric1/api-key-sniffer.git
cd api-key-sniffer
```

## Usage
To run the program:
```bash
python main.py <directory> --config <config_file>
```

### Example
```bash
python main.py ./my_project --config config.json
```

Use `--help` to get more information about parameters

## Configuration
By default the config file is `config.json`, this can be changed by the ``--config`` parameter.

The config file allows for the configuration of
- Which API key patterns to scan for (`enabled_patterns`).
- The maximum depth for directory scanning (`max_depth`).
- Whether logging is enabled (`enable_logging`).
- The log file name (`log_file`).

### Example Config File
```json
{
  "enabled_patterns": ["AWS Access Key", "Google API Key"],
  "max_depth": 3,
  "enable_logging": true,
  "log_file": "scan_log.txt"
}
```

## License
See [LICENSE](LICENSE)
