from shutil import rmtree
import os

def copy_source_to_dest(source, dest):
    if os.path.exists(dest):
        print(f'Deleting stale destination directory "{dest}".')
        rmtree(dest)
    print(f'Creating destination directory "{dest}".')
    os.mkdir(dest)
