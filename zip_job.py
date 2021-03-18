import os
import pathlib
import sys
from zipfile import ZipFile

version = os.environ.get('VERSION')
names_array = ["a","b","c","d"]

for name in names_array:
    file_name = "{name}.txt".format(name=name)
    wanted_file = "./{file_name}".format(file_name=file_name)
    if not os.path.exists(wanted_file):
        os.mknod(wanted_file)
        file_path = pathlib.Path(wanted_file)
        if not file_path.exists():
            error_msg = "{file_path} does not exist.".format(file_path=file_path)
            sys.exit(error_msg)

    # create a ZipFile object
    full_zip_name = "{name}_{version}.zip".format(name=name, version=version)
    zipObj = ZipFile(full_zip_name, 'w')
    # Add multiple files to the zip
    zipObj.write(file_name)
    # close the Zip File
    zipObj.close()

    wanted_zip_file = "./{full_zip_name}".format(full_zip_name=full_zip_name)
    zip_file_path = pathlib.Path(wanted_zip_file)
    if not zip_file_path.exists():
        error_msg = "{wanted_zip_file} does not exist.".format(wanted_zip_file=wanted_zip_file)
        sys.exit(error_msg)