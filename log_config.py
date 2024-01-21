import time
from pathlib import Path

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": '%(asctime)s | %(pathname)s [line:%(lineno)d] | %(levelname)s: %(message)s',
            "use_colors": False,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '|%(asctime)s | %(levelname)s | %(client_addr)s | "%(request_line)s" | %(status_code)s| Process: %(process)d |',
            "use_colors": False,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "filelog_default": {
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": Path(f'logs/app.log'),
            "encoding": "utf8",
            "backupCount": 5,
            "when": "midnight",
        },
        "filelog_access": {
            "formatter": "access",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": Path(f'logs/app_access.log'),
            "encoding": "utf8",
            "backupCount": 5,
            "when": "midnight",
        },
    },
    "loggers": {
        "": {"handlers": ["default", "filelog_default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {
            "handlers": ["access", "filelog_access"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
