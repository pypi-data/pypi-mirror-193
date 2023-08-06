import logging
from logging import StreamHandler

logger = logging.getLogger("atfdb")


def configure_logger(logger, log_level=logging.DEBUG, handlers=[StreamHandler]):
    log_file_format = "[%(levelname)1.1s %(asctime)s %(name)s %(module)s:%(lineno)d] %(message)s"
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    for handler_class in handlers:
        handler = handler_class()
        handler.setFormatter(logging.Formatter(fmt=log_file_format))
        logger.addHandler(handler)
        handler.setLevel(log_level)
