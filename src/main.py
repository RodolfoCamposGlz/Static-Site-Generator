import os
import shutil
import re
from textnode import TextNode
from block_markdown import (markdown_to_html_node)
from pathlib import Path

path_destination= "public"

markdown = """
# This is a heading

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

dir_path_content = "content"
template_path ="template.html"
dest_dir_path="public"


def main():
    delete_files()
    copy_files('static')
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
    # generate_page(from_path, template_path, dest_path)
    
def copy_files(path):
    if not os.path.exists(path) or os.path.isfile(path):
        return
    
    list_paths = os.listdir(path)
    for list in list_paths:
        src = f"{path}/{list}"
        if(not os.path.isfile(src)):
            new_path = os.path.join(path_destination, src)
            new_path = new_path.replace("static/", "")
            if not os.path.exists(path_destination):
                os.mkdir('public')
            os.mkdir(new_path)
        else:
            new_destination = src.replace("static/", "")
            shutil.copy(src, f"{path_destination}/{new_destination}")
        copy_files(src)

def delete_files():
    if os.path.exists(path_destination):
        for item in os.listdir(path_destination):
            item_path = os.path.join(path_destination, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def extract_title(html_node):
    html = html_node.to_html()

    match = re.search(r'<h1>(.*?)</h1>', html)
    if match:
        return match.group(1)
    else:
        raise Exception("Title not found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content) or os.path.isfile(dir_path_content):
        return
    list_paths = os.listdir(dir_path_content)
    for list in list_paths:
        src = os.path.join(dir_path_content, list)
        current_path = Path(src)
        destination = os.path.join(dest_dir_path, list)

        if os.path.isdir(current_path):
            if not os.path.exists(destination) and os.listdir(current_path) != []:
                os.mkdir(destination)
        else:
            with open(current_path) as f:
                read_markdown = f.read()
                f.close()
            with open(template_path) as f:
                read_template = f.read()
                f.close()
            html_node = markdown_to_html_node(read_markdown)
            title = extract_title(html_node)
            read_template = read_template.replace("{{ Title }}", title)
            read_template = read_template.replace("{{ Content }}", html_node.to_html())
            create_html_file(dest_dir_path, read_template)

        generate_pages_recursive(src, template_path, destination)

def create_html_file (path, new_template):
    file_path = os.path.join(path, "index.html")
    with open(file_path, 'w') as file:
        return file.write(new_template)

main()