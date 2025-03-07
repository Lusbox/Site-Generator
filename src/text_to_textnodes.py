import re
from textnode import *
from htmlnode import *
from split_nodes import *
from text_to_html import *
from extract_markdown_images import *

def text_to_textnodes(text):
	if text == "":
		return [TextNode("", TextType.TEXT)]
	nodes = [TextNode(text, TextType.TEXT)]
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)
	return nodes
