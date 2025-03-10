import os
import re

from markdown_to_html import *
from htmlnode import *
from extract_title import *

def generate_page(from_path, template_path, dest_path, basepath):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	if os.path.isfile(os.path.join(from_path)):
		with open(os.path.join(from_path), 'r') as file:
			md_content = file.read()
	else:
		raise Exception (f"No readable file at the provided path: {from_path}")

	if os.path.isfile(os.path.join(template_path)):
		with open(os.path.join(template_path), 'r') as file:
			template_content = file.read()
	else:
		raise Exception (f"No readable file at the provided path: {template_path}")


	node = markdown_to_html_node(md_content)
	html_string = node.to_html()

	title = extract_title(md_content)

	template = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
	template = template.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

	dir_path = os.path.dirname(dest_path)
	os.makedirs(dir_path, exist_ok=True)

	with open(dest_path, 'w') as file:
		file.write(template)
