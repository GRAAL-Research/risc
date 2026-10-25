from importlib.metadata import PackageNotFoundError, version

from .content import *
from .domain import *
from .faker import *
from .model import *

try:
    __version__ = version("risc_generator")
except PackageNotFoundError:  # Running from a source checkout without installing the package.
    __version__ = "unknown"
