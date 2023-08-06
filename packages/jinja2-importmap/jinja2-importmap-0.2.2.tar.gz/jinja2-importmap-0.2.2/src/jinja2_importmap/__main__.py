import sys
from pathlib import Path

import click

from .core import scan_packages

if sys.version_info < (3, 9):
    import importlib_resources as resources
    from importlib.abc import Traversable
else:
    from importlib import resources
    from importlib.abc import Traversable


@click.command()
@click.argument("input-dir", type=click.Path(), default=None)
@click.option("--package", type=str, default=None, help="Package to scan.")
@click.option("--prefix", type=str, default="/statics/vendor",
              help="Prefix to use for importmap values.")
@click.option("--indent", type=int, default=4,
              help="Indentation to use for JSON output.")
@click.argument("output-file", type=click.File("w"), default="-", required=False)
def main(input_dir, package, prefix, indent, output_file):
    modules_root: Path | Traversable
    if package:
        modules_root = resources.files(package) / input_dir
    else:
        modules_root = Path(input_dir)

    if not modules_root.is_dir():
        raise click.BadParameter(
            f"modules_dir must be a directory, got {modules_root!r}"
        )

    import_map = scan_packages(modules_root, prefix=prefix)
    output_file.write(import_map.json(indent=indent))


if __name__ == "__main__":
    main()
