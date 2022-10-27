"""
Відсортувати файли в папці.
"""

import argparse
from pathlib import Path
from shutil import copyfile
from multiprocessing import Pool, cpu_count

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


def grabs_folder(path: Path) -> list:
    folders = []
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            r = grabs_folder(el)
            if len(r):
                folders = folders + r
        else:
            ...
    return folders


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as err:
                print(err)


if __name__ == '__main__':
    base_folder = Path(source)

    with Pool(cpu_count()) as pool:
        pool.map(copy_file, grabs_folder(base_folder))
        pool.close()
        pool.join()

    print('Можно удалять стару папку якщо треба')
