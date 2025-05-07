import logging

def setup_logging(enable, filename, level=logging.INFO):
    """Sets up logging configuration."""
    if enable:
        logging.basicConfig(
            filename=filename,
            level=level,
            format='%(asctime)s - %(message)s'
        )
    else:
        logging.disable(logging.CRITICAL)