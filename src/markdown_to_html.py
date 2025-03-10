import re

from htmlnode import *
from extract_markdown_images import *
from markdown_to_blocks import *
from text_to_textnodes import *
from text_to_html import *
from blocktype import *
from textnode import *
from enum import Enum

def markdown_to_html_node(markdown):
	blocks = markdown_to_blocks(markdown)
	div = HTMLNode("div", None)
	div.children = []

	for block in blocks:
		if not block.strip():
			continue

		block_type = block_to_block_type(block)

		if block_type == BlockType.QUOTE:
			q_node = HTMLNode("blockquote", None)
			cleaned_block = "\n".join([line.lstrip('>').strip() for line in block.split('\n')])
			children = text_to_children(cleaned_block)
			q_node.children = children
			div.children.append(q_node)

		if block_type == BlockType.PARAGRAPH:
			p_node = HTMLNode("p", None)
			paragraph_content = re.sub(r"\n", " ", block)
			children = text_to_children(paragraph_content)
			p_node.children = children
			div.children.append(p_node)

		if block_type == BlockType.HEADING:
			level = 0
			for char in block:
				if char == '#':
					level += 1
				else:
					break
			h_node = HTMLNode(f"h{level}", None)
			heading_content = block[level:].strip()
			children = text_to_children(heading_content)
			h_node.children = children
			div.children.append(h_node)

		if block_type == BlockType.UNORDERED_LIST:
			ul_node = HTMLNode("ul", None)
			ul_node.children = []

			items = re.split(r"\n", block)

			for item in items:
				if not item.strip():
					continue

				item_content = re.sub(r"^[-*]\s+", "", item.strip())
				li_node = HTMLNode("li", None)
				li_node.children = text_to_children(item_content)
				ul_node.children.append(li_node)

			div.children.append(ul_node)

		if block_type == BlockType.ORDERED_LIST:
			ol_node = HTMLNode("ol", None)
			ol_node.children = []

			items = re.split(r"\n", block)

			for item in items:
				if not item.strip():
					continue

				item_content = re.sub(r"^\d+\.\s+", "", item.strip())
				li_node = HTMLNode("li", None)
				li_node.children = text_to_children(item_content)
				ol_node.children.append(li_node)

			div.children.append(ol_node)

		if block_type == BlockType.CODE:
			pre_node = HTMLNode("pre", None)
			code_node = HTMLNode("code", None)

			code_content = block.strip()
			if code_content.startswith("```"):
				code_content = code_content[3:]
			if code_content.endswith("```"):
				code_content = code_content[:-3]
			code_content = code_content.strip()

			if not code_content.endswith("\n"):
				code_content += "\n"

			text_node = TextNode(code_content, TextType.TEXT)
			html_node = text_node_to_html_node(text_node)

			code_node.children = [html_node]
			pre_node.children = [code_node]

			div.children.append(pre_node)

	return div



def text_to_children(text):
	nodes = text_to_textnodes(text)
	html_nodes = []
	for node in nodes:
		html_node = text_node_to_html_node(node)
		html_nodes.append(html_node)
	return html_nodes



def heading_number(text):
	match = re.match(r"^(#{1,6})", text)
	if match:
		level = len(match.group(1))
		return f"h{level}"
	return "h1"




