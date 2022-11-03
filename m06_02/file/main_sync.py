"""
Відсортувати файли в папці.
"""

import argparse
import asyncio

from pathlib import Path
from shutil import copyfile

"""
--source [-s] picture
--output [-o]
"""

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")
output_folder = Path(output)


def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            copy_file(el)


def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    try:
        new_path.mkdir(exist_ok=True, parents=True)
        copyfile(file, new_path / file.name)
    except OSError as err:
        print(err)


if __name__ == '__main__':
    base_folder = Path(source)
    read_folder(base_folder)
