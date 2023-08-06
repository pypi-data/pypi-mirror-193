# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
# pylint: disable=bare-except
# pylint: disable=line-too-long
# pylint: disable=unused-import

'''
    Contains the directory class

    ----------

    Meta
    ----------
    `author`: Colemen Atwood
    `created`: 06-04-2022 10:44:23
    `memberOf`: directory_utils
'''


from datetime import datetime
from re import L
import colemen_utilities.directory_utils.dir_compression as _comp
import colemen_utilities.file_utils as _f
# import colemen_utilities.dict_utils as _obj
# import colemen_utilities.string_utils as _csu

# logger = _logging.getLogger(__name__)
from dataclasses import dataclass
import os
from typing import Union



@dataclass
class Directory:
    file_path:str = None
    '''The path to this directory'''
    name:str = None
    '''The name of this directory.'''
    dir_path:str = None
    '''The path to the directory that contains this directory.'''
    _modified = None
    _accessed = None
    _created = None
    _size = None

    def __init__(self,file_path:str) -> None:
        self.file_path = file_path
        self.dir_path = os.path.dirname(file_path)
        self.name = os.path.basename(file_path)


    # ---------------------------------------------------------------------------- #
    #                                TIMESTAMP SHIT                                #
    # ---------------------------------------------------------------------------- #
    
    @property
    def modified(self):
        '''
            Get this dir's modified

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-22-2023 16:39:24
            `@memberOf`: dir
            `@property`: modified
        '''
        value = self._modified
        if value is None:
            value = os.path.getmtime(self.file_path)
            self._modified = value
        return value

    @modified.setter
    def modified(self,value:float):
        '''
            Set the modified time for this directory.

            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:10:50
            `@memberOf`: PostArg
            `@property`: access
        '''
        os.utime(self.file_path, (self.accessed,value))
        value = os.path.getmtime(self.file_path)
        self._modified = value

    @property
    def modified_mdy(self):
        '''
            Get this dir's modified_timestamp as m-d-y

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:15:12
            `@memberOf`: dir
            `@property`: modified_pretty
        '''

        value = timestamp_to_pretty(self.modified,'%m-%d-%Y')
        return value

    @property
    def modified_datetime(self):
        '''
            Get this dir's modified timestamp as a datetime object.

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:16:36
            `@memberOf`: dir
            `@property`: modified_datetime
        '''
        value = datetime.fromtimestamp(self.modified)
        return value



    @property
    def accessed(self):
        '''
            Get this dir's accessed

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-22-2023 16:39:24
            `@memberOf`: dir
            `@property`: accessed
        '''
        value = self._accessed
        if value is None:
            value = os.path.getatime(self.file_path)
            self._accessed = value
        return value

    @accessed.setter
    def accessed(self,value:float):
        '''
            Set the accessed time for this directory.

            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:10:50
            `@memberOf`: PostArg
            `@property`: access
        '''
        os.utime(self.file_path, (self.accessed,value))
        value = os.path.getmtime(self.file_path)
        self._accessed = value

    @property
    def accessed_mdy(self):
        '''
            Get this dir's accessed_timestamp as m-d-y

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:15:12
            `@memberOf`: dir
            `@property`: accessed_pretty
        '''

        value = timestamp_to_pretty(self.accessed,'%m-%d-%Y')
        return value

    @property
    def accessed_datetime(self):
        '''
            Get this dir's accessed timestamp as a datetime object.

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:16:36
            `@memberOf`: dir
            `@property`: accessed_datetime
        '''
        value = datetime.fromtimestamp(self.accessed)
        return value


    @property
    def created(self):
        '''
            Get this dir's created

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-22-2023 16:39:24
            `@memberOf`: dir
            `@property`: created
        '''
        value = self._created
        if value is None:
            value = os.path.getmtime(self.file_path)
            self._created = value
        return value

    @property
    def created_mdy(self):
        '''
            Get this dir's created_timestamp as m-d-y

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:15:12
            `@memberOf`: dir
            `@property`: created_pretty
        '''

        value = timestamp_to_pretty(self.created,'%m-%d-%Y')
        return value

    @property
    def created_datetime(self):
        '''
            Get this dir's created timestamp as a datetime object.

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:16:36
            `@memberOf`: dir
            `@property`: created_datetime
        '''
        value = datetime.fromtimestamp(self.created)
        return value



    @property
    def size(self):
        '''
            Get this dir's size in bytes

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 09:02:37
            `@memberOf`: dir
            `@property`: size
        '''
        value = self._size
        # if value is None:
        size = 0
        for path, dirs, files in os.walk(self.file_path):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)

        value = size
        return value

    def create_zip(self,file_name:str = None,delete_after:bool=False,
                overwrite:bool=True):
        '''
            Convert this directory to a zip file.

            ----------

            Arguments
            -------------------------
            `file_name` {str}
                The name of the zip file.
                If not provided, the directory name will be used.

            [`delete_after`=False] {bool}
                Delete the original directory after the zip file is made.

            [`overwrite`=True] {bool}
                If False, it will skip creating the archive.


            Return {bool}
            ----------------------
            True upon success, false otherwise.

            Meta
            ----------
            `author`: Colemen Atwood
            `created`: 02-22-2023 16:44:53
            `memberOf`: dir
            `version`: 1.0
            `method_name`: create_zip
            * @xxx [02-22-2023 16:47:06]: documentation for create_zip
        '''
        if file_name is None:
            file_name = self.name
        dst = f"{self.dir_path}/{self.name}"

        return _comp.create_zip(self.file_path,dst,delete_after=delete_after,overwrite=overwrite)

    @property
    def files(self):
        '''
            Get this dir's files

            `default`:None


            Meta
            ----------
            `@author`: Colemen Atwood
            `@created`: 02-23-2023 08:34:16
            `@memberOf`: dir
            `@property`: files
        '''
        value = _f.get_files(self.file_path,recursive=False)
        return value

def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def timestamp_to_pretty(timestamp,format_string:str=None):
    if format_string is None:
        format_string = "%m-%d-%Y %H:%M:%S:%f"
    return datetime.fromtimestamp(timestamp).strftime(format_string)
