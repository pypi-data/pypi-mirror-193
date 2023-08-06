from typing import List, Union

from jinja2 import Environment
from jinja2.nodes import Node
from jinja2.ext import Extension
from jinja2.parser import Parser

from .core import scan_packages


class ImportMapExtension(Extension):

    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.globals["importmap"] = scan_packages

    def parse(self, parser: Parser) -> Union[Node, List[Node]]:
        raise NotImplementedError


importmap = ImportMapExtension
