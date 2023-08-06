import json
import sys
from collections.abc import MutableMapping
from pathlib import Path
from typing import Dict, Optional

if sys.version_info < (3, 9):
    from importlib_resources.abc import Traversable
else:
    from importlib.abc import Traversable

from pydantic import BaseModel


# TODO:
# [ ] - Allow specifying location of package.json, read .yarnrc?
# [ ] - Support for Bower (probably not?)


class ImportMap(BaseModel, MutableMapping[str, str]):
    imports: Dict[str, str] = {}

    def __getitem__(self, key: str) -> str:
        return self.imports[key]

    def __setitem__(self, key, value) -> None:
        self.imports[key] = value

    def __delitem__(self, key: str) -> None:
        del self.imports[key]

    def __len__(self) -> int:
        return len(self.imports)


# Enum?

def _scan_package(module_path: Path | Traversable, scope=None) -> Optional[str]:
    """
    Given a module_path, if it is an ES6 module, return the module name
    from its package.json. Otherwise, return None.
    :param module_path:
    :return:
    """

    package_json = module_path / "package.json"
    if not package_json.is_file():
        return None

    package_json = package_json.read_text()
    package_json = json.loads(package_json)
    if "module" not in package_json:
        return None

    return f"{scope + '/' if scope else ''}{module_path.name}/{package_json['module']}"


def scan_packages(modules_root: Optional[Path | Traversable] = None,
                  prefix: str = "/statics/vendor") -> ImportMap:
    """
    Construct an import map by scanning a directory of ES6 modules. We assume that
    this directory follows the usual node_modules structure:

    - Each subdirectory is a package or a group of packages (prefixed with @).
    - The root of each package contains a package.json file.
    - The "module" field of the package.json file is the module name.

    The mapping is then constructed as:

    {
        "imports": {
            "[@group]/package-name": "/path/to/module/defined/in/package.json"
        }
    }

    :param modules_root: Path or importlib Traversable to scan. Defaults to
                        `node_modules` in the current working directory.
    :param prefix: Prefix to prepend to the importmap values (URLs to module indices).
    :return: An import map for the given root.
    """
    if modules_root is None:
        modules_root = Path.cwd() / "node_modules"

    modules_root: Traversable

    if not modules_root.is_dir():
        raise ValueError("modules must be a directory")

    prefix = prefix.rstrip("/")

    import_map = ImportMap()
    for package_dir in modules_root.iterdir():
        if package_dir.name.startswith('@'):
            scope_dir = package_dir
            # Scoped packages
            for scoped_package_dir in scope_dir.iterdir():
                package_name = f"{scope_dir.name}/{scoped_package_dir.name}"
                module_index = _scan_package(scoped_package_dir, scope=scope_dir.name)
                import_map[package_name] = f"{prefix}/{module_index}"
        else:
            # Single package
            package_name = package_dir.name
            module_index = _scan_package(package_dir)
            import_map[package_name] = f"{prefix}/{module_index}"

    return import_map
