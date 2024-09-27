import logging
import logging.config
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "application.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Logger Configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    }
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    return logger

# Call this function in your apps
logger = setup_logging()
