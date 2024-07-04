import os
import shutil
import re
from textnode import TextNode
from block_markdown import (markdown_to_html_node)

path_destination= "public"

markdown = """
# This is a heading

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

from_path = "content/index.md"
template_path ="template.html"
dest_path="public"


def main():
    delete_files()
    copy_files('static')
    generate_page(from_path, template_path, dest_path)
    
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
            
            pass
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
        print("grab_content", match.group(1))
        return match.group(1)
    else:
        raise Exception("Title not found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        read_markdown = f.read()
        f.close()

    with open(template_path) as f:
        read_template = f.read()
        f.close()

    html_node = markdown_to_html_node(read_markdown)
    title = extract_title(html_node)
    read_template = read_template.replace("{{ Title }}", title)
    read_template = read_template.replace("{{ Content }}", html_node.to_html())

    def create_html_file (path):
        file_path = os.path.join(path, "index.html")
        with open(file_path, 'w') as file:
            return file.write(read_template)
        
    if os.path.exists(dest_path):
        create_html_file(dest_path)
    else:
        os.mkdir('public')
        create_html_file(dest_path)
main()