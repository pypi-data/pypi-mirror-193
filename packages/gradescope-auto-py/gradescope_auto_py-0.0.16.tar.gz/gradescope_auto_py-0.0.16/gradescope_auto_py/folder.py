import pathlib
import shutil
import tempfile
from contextlib import contextmanager


@contextmanager
def to_temp_folder(file_tup=tuple(), file_str_dict=None):
    """ moves files (and str) to a temporary folder, deletes when done

    Args:
        file_tup (tuple): files to move
        file_str_dict (dict): keys are str (files), values are strs to write to
            those files
    Returns:
        folder (pathlib.Path): temporary folder
    """
    # make temp directory
    folder_tmp = pathlib.Path(tempfile.mkdtemp())

    # copy files to be included
    for file in file_tup:
        file = pathlib.Path(file)
        shutil.copy(file, folder_tmp / file.name)

    # print text files
    if file_str_dict is not None:
        for file, s in file_str_dict.items():
            with open(folder_tmp / file, 'w') as f:
                print(s, file=f)

    yield folder_tmp

    # cleanup temp folder
    shutil.rmtree(folder_tmp)
