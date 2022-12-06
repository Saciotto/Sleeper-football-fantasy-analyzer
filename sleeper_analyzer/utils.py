import json
from pathlib import Path


def load_json_file(file_path):
    with file_path.open() as fp:
        value = json.load(fp)
    return value


def rm_tree(folder):
    folder = Path(folder)
    if folder.exists():
        for child in folder.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                rm_tree(child)
        folder.rmdir()
