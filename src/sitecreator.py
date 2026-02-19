from shutil import rmtree
from shutil import copy
import os

def copy_source_to_dest(source, dest, refresh=True):
    if os.path.exists(dest) and refresh:
        print(f'Deleting stale destination directory "{dest}".')
        rmtree(dest)
    print(f'Creating destination directory "{dest}".')
    os.mkdir(dest)

    contents_of_dir = os.listdir(source)
    for file_object in contents_of_dir:
        source_file_object = os.path.join(source, file_object)
        dest_file_object = os.path.join(dest, file_object)
        print(f'Source file object: "{source_file_object}"')
        print(f'Destination file object "{dest_file_object}"')
        if os.path.isdir(source_file_object):
            print(f'Entering directory "{source_file_object}"')
            copy_source_to_dest(source_file_object, dest_file_object, False)
        else:
            print("Copying file.")
            copy(source_file_object, dest_file_object)


