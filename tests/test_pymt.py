import pytest

import os
import sys
from app.pymt import _create_file

correct_filepaths = [
    'test',
    'test.py',
    'test/test',
    'test/test.py'
]
wrong_filepaths = [
    '/test',
    '/test.py',
    '/test/test',
    '/test/test.py'

]

class TestCreatePyFiles:

    @pytest.mark.parametrize('filepath',correct_filepaths)
    def test_run(self, tmpdir,filepath):
        current_dir = tmpdir.mkdir('tmpdir')
        os.chdir(current_dir)

        expected_path = f"{filepath}"
        if filepath.endswith('.py') is False:
            expected_path += '.py'

        assert os.path.exists(expected_path) is False
        _create_file(filepath)
        assert os.path.exists(expected_path) is True

    @pytest.mark.parametrize('filepath',correct_filepaths)
    def test_already_exists_error(self, tmpdir,filepath):
        current_dir = tmpdir.mkdir('tmpdir')
        os.chdir(current_dir)
        expected_path = f"{filepath}"
        if filepath.endswith('.py') is False:
            expected_path += '.py'
        dirname = os.path.dirname(filepath)

        if dirname:
            os.makedirs(dirname)

        f = open(expected_path, 'w')
        f.close()
        assert os.path.exists(expected_path) is True
        with pytest.raises(FileExistsError):
            _create_file(filepath)

    @pytest.mark.parametrize('filepath',wrong_filepaths)
    def test_root_path(self, tmpdir, filepath):
        current_dir = tmpdir.mkdir('tmpdir')
        os.chdir(current_dir)

        with pytest.raises(ValueError):
            _create_file(filepath)



