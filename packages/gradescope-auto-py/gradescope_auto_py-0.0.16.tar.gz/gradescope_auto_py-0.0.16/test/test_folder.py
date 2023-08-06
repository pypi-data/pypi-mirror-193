from gradescope_auto_py.folder import *


def test_folder():
    file_str_dict = {'test.txt': 'contents of test.txt'}
    with to_temp_folder(file_str_dict=file_str_dict) as folder:
        assert folder.exists()
    assert not folder.exists()
