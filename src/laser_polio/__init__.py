from .distributions import *  # noqa F403
from .pars import *  # noqa F403
from .model import *  # noqa F403
from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

# from .seir_mpm import *
from .utils import *  # noqa F403

try:
    __version__ = version("laser-polio")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

root = Path(__file__).resolve().parents[2]
