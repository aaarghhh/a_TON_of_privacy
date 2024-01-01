import os
import sys
import errno
import math

ERROR_INVALID_NAME = 123


class Util:
    def __init__(self):
        pass

    @staticmethod
    def is_pathname_valid(pathname: str) -> bool:
        """
        `True` if the passed pathname is a valid pathname for the current OS;
        `False` otherwise.
        """
        try:
            if not isinstance(pathname, str) or not pathname:
                return False

            _, pathname = os.path.splitdrive(pathname)
            root_dirname = (
                os.environ.get("HOMEDRIVE", "C:")
                if sys.platform == "win32"
                else os.path.sep
            )
            assert os.path.isdir(root_dirname)
            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                except OSError as exc:
                    if hasattr(exc, "winerror"):
                        if exc.winerror == ERROR_INVALID_NAME:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        except TypeError as exc:
            return False
        else:
            return True

    @staticmethod
    def get_file_size(self, path):
        return os.path.getsize(path)

    @staticmethod
    def get_file_size_human(self, path):
        size = self.get_file_size(path)
        return self.convert_size(size)

    @staticmethod
    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])
