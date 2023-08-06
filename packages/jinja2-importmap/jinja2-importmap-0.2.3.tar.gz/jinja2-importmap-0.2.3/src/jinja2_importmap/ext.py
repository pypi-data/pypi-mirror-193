import sys

if sys.version_info < (3, 9):
    import importlib_resources as resources
else:
    from importlib import resources
from pathlib import Path
from typing import List, Union

from jinja2 import Environment
from jinja2.nodes import Node
from jinja2.ext import Extension
from jinja2.parser import Parser

from .core import scan_packages


def _importmap(modules_root, package=None, prefix="/statics/vendor"):
    """
    Temporary solution until parse is implemented...
    """
    if package:
        modules_root = resources.files(package) / modules_root
    else:
        modules_root = Path(modules_root)

    return scan_packages(modules_root, prefix=prefix).imports


class ImportMapExtension(Extension):

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.globals["importmap"] = _importmap

    def parse(self, parser: Parser) -> Union[Node, List[Node]]:
        raise NotImplementedError


importmap = ImportMapExtension
