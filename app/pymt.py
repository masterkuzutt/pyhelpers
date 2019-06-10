import os
import sys


def create_py_files(filepath, test_prefix='test',test_dir='tests'):
    _create_file(filepath)
    test_filepath = "/".join([test_dir, f"{test_prefix}_{filepath}"])
    _create_file(test_filepath)


def _create_file(filepath):
    if filepath.startswith('/') is True:
        raise ValueError(f"Can not create file from root: {filepath}")

    if filepath.endswith('.py') is False:
        filepath += '.py'

    if os.path.exists(filepath):
        raise FileExistsError(filepath)

    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

    f = open(filepath, 'w')
    f.close()


def main():
    create_py_files(*sys.argv[1:])

