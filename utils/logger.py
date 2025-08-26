import logging


def get_logger(name: str = __name__) -> logging.Logger:
    """Returns a configured logger that can be reused across the project"""
    logger = logging.getLogger(name)

    if not logger.handlers:  # Prevent adding multiple handlers
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
