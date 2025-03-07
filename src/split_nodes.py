import re

from textnode import *
from htmlnode import *
from extract_markdown_images import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		text = node.text
		parts = []

		while True:
			start = text.find(delimiter)
			if start == -1:
				if text:
					parts.append((text, TextType.TEXT))
				break
			if start > 0:
				parts.append((text[:start], TextType.TEXT))

			end = text.find(delimiter, start + len(delimiter))
			if end == -1:
				raise Exception ("invalid Markdown syntax")

			delimited_text = text[start + len(delimiter):end]
			parts.append((delimited_text, text_type))

			text = text[end + len(delimiter):]

		for part_text, part_type in parts:
			new_nodes.append(TextNode(part_text, part_type))


	return new_nodes



def split_nodes_image(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		text = node.text
		images = extract_markdown_images(text)

		if not images:
			new_nodes.append(node)
			continue

		remaining_text = text
		for alt_text, url in images:
			image_markdown = f"![{alt_text}]({url})"
			parts = remaining_text.split(image_markdown, 1)

			if parts[0]:
				new_nodes.append(TextNode(parts[0], TextType.TEXT))

			new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

			if len(parts) > 1:
				remaining_text = parts[1]
			else:
				remaining_text = ""

		if remaining_text:
			new_nodes.append(TextNode(remaining_text, TextType.TEXT))

	return new_nodes

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
			continue
		text = node.text
		links = extract_markdown_links(text)

		if not links:
			new_nodes.append(node)
			continue

		remaining_text = text
		for alt_text, url in links:
			link_markdown = f"[{alt_text}]({url})"
			parts = remaining_text.split(link_markdown, 1)

			if parts[0]:
				new_nodes.append(TextNode(parts[0], TextType.TEXT))

			new_nodes.append(TextNode(alt_text, TextType.LINK, url))

			if len(parts) > 1:
				remaining_text = parts[1]
			else:
				remaining_text = ""

		if remaining_text:
			new_nodes.append(TextNode(remaining_text, TextType.TEXT))

	return new_nodes
