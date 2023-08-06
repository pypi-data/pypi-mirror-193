import hashlib
import json
import pathlib
import tempfile

import gradescope_auto_py as gap
from gradescope_auto_py.grader_config import GraderConfig

hw0_folder = pathlib.Path(gap.__file__).parents[1] / 'test' / 'ex' / 'hw0'


def all_files_equal(file_tup):
    """ compares a tuple of files, True if all files are identical """
    # https://stackoverflow.com/questions/31027268/pythonfunction-that-compares-two-zip-files-one-located-in-ftp-dir-the-other
    hash_tup = tuple(hashlib.sha256(open(file, 'rb').read()).digest()
                     for file in file_tup)
    return all(hash_tup[0] == hash for hash in hash_tup[2:])


def test_grader_config():
    # test __init__ & from_py()
    grader_config = GraderConfig.from_py(folder_local='ex/hw0',
                                         file_afp='hw0.py',
                                         file_run='hw0_stud.py')

    # test from_json()
    file_config_json = hw0_folder / 'hw0_grader_config.json'
    grader_config_exp = GraderConfig.from_json(file_config_json)
    assert grader_config.__dict__ == grader_config_exp.__dict__

    # test to_json()
    file = tempfile.NamedTemporaryFile(suffix='.json').name
    grader_config.to_json(file=file)
    grader_config2 = GraderConfig.from_json(file=file)
    assert grader_config2.__dict__ == grader_config.__dict__

    # test make_autograder()
    file_zip = tempfile.NamedTemporaryFile(suffix='auto.zip').name
    grader_config.build_autograder(file_zip=file_zip)
    assert all_files_equal(file_tup=(file_zip, hw0_folder / 'hw0_auto.zip'))

    # test grade() (just test output is created, behavior tested elsewhere)
    grader = grader_config.grade(folder_submit=hw0_folder / 'case_syntax_error',
                                 folder_source=hw0_folder)

    # confirm expected outputs
    file_json_expected = hw0_folder / 'case_syntax_error' / 'results.json'
    with open(file_json_expected, 'r') as f:
        json_expected = json.load(f)

    assert json_expected == grader.get_json()
