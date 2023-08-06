from ._version import get_versions
from .utils import configure_logger, logger  # noqa F401

__version__ = get_versions()["version"]
del get_versions
