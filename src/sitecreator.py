from shutil import rmtree
from shutil import copy
import os
from markdownparse import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

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

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING and block.startswith("# "):
            block = block.replace("# ", "", 1)
            block = block.strip()
            return block

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from "{from_path}" to "{dest_path}" using "{template_path}".')
    with open(from_path, 'r') as f:
        md = f.read()

    node = markdown_to_html_node(md)
    #print("*******HTML********")
    #print(f"{node.to_html()}")
    #print("*****NODE*********")
    #print(f"{node}")
    
    with open(template_path, 'r') as f:
        template = f.read()

    template = template.replace("{{ Title }}", extract_title(md))
    template = template.replace("{{ Content }}", node.to_html())

    path = os.path.dirname(dest_path)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(dest_path, 'w') as f:
        f.write(template)

    
    
