from textnode import *
from htmlnode import *


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
