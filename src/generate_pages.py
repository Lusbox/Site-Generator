import os
import re

from markdown_to_html import *
from htmlnode import *
from extract_title import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	path_list = os.listdir(dir_path_content)
	for path in path_list:
		full_item_path = os.path.join(dir_path_content, path)
		relative_path = os.path.relpath(full_item_path, dir_path_content)
		dest_item_path = os.path.join(dest_dir_path, relative_path)


		if os.path.isdir(full_item_path):
			os.makedirs(os.path.join(dest_dir_path, relative_path), exist_ok=True)

			generate_pages_recursive(full_item_path, template_path, dest_item_path)

		elif full_item_path.endswith('.md'):
			with open(full_item_path, 'r') as file:
				md_content = file.read()

			with open(template_path, 'r') as file:
				template_content = file.read()

			node = markdown_to_html_node(md_content)
			html_string = node.to_html()

			title = extract_title(md_content)

			template = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

			dest_html_path = dest_item_path.replace('.md', '.html')

			dir_path = os.path.dirname(dest_html_path)
			os.makedirs(dir_path, exist_ok=True)

			with open(dest_html_path, 'w') as file:
				file.write(template)


