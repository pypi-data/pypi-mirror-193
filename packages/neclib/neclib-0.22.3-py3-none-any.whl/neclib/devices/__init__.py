import importlib
import sys
from pathlib import Path

from . import selector

paths = Path(__file__).parent.iterdir()
module_paths = filter(lambda p: p.is_dir() and p.name[0] not in "._", paths)
impl_modules = [
    importlib.import_module(f".{m.name}", __package__) for m in module_paths
]  # This is necessary for subclass search in `device_base.get_device_list()`

implementations = selector.list_implementations()
"""List of all available implementations."""

parsed = selector.parse_device_configuration()
"""List of parsed device implementations."""

here = sys.modules[__name__]
_ = [setattr(here, k, v) for k, v in parsed.items()]
