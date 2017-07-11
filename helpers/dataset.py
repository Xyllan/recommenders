from os import listdir
from os.path import isfile, isdir, join
from zipfile import ZipFile
from pandas import read_csv

_valid_archive_types = ['dir', 'zip']


class Dataset:
    """ Represents a dataset.
    Dataset can be a directory (in which case its child files will be considered),
    or a zip file (in which case it will not be extracted, but will be read into memory if needed).
    Args:
        name: name of the dataset under the datasets folder
        archive_type: either a directory ('dir') or a zip file ('zip')
    """
    def __init__(self, name, archive_type = None):
        self.name = name
        self._archive_type = archive_type
        if self._archive_type not in _valid_archive_types:
            self._find_archive_type()
        self._load_archive()

    def _find_archive_type(self):
        base_path = join('datasets', self.name)
        if isdir(base_path):
            self._archive_type = 'dir'
        elif isfile(join(base_path, 'zip')):
            self._archive_Type = 'zip'
        else:
            raise ValueError('A dataset of a compatible type was not found')

    def _load_archive(self):
        base_path = join('datasets', self.name)
        if self._archive_type is 'dir':
            self.base_path = base_path
            self.file = None
        elif self._archive_type is 'zip':
            self.base_path = base_path + '.zip'
            self.file = ZipFile(self.base_path, 'r')

    def filenames(self):
        if self._archive_type is 'dir':
            return [f for f in listdir(self.base_path) if isfile(join(self.base_path, f))]
        elif self._archive_type is 'zip':
            return self.file.namelist()

    def file_pointer(self, filename):
        """ Returns a file pointer to the given filename. """
        if self._archive_type is 'dir':
            return open(join(self.base_path, filename), 'r')
        elif self._archive_type is 'zip':
            return self.file.open(filename, 'r')

    def load_dataframe(self, filename):
        """ Loads a given CSV file into a Pandas dataframe. """
        return read_csv(self.file_pointer(filename))

    def close(self):
        if self.file:
            self.file.close()
