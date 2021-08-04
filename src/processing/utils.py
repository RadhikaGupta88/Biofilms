import pathlib

def list_files(path):
    path = pathlib.Path(path)
    assert path.exists(), "Path does not exist."
    return list(path.glob("*"))