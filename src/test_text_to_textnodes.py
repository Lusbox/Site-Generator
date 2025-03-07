import unittest

from text_to_textnodes import *

class TestTextTo(unittest.TestCase):
	def test_eq(self):
		text = ("This is **text** with an _italic_ word "
			"and a `code block` "
			"and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
			"and a [link](https://boot.dev)")
		new_node = text_to_textnodes(text)
		self.assertEqual([
				TextNode("This is ", TextType.TEXT),
				TextNode("text", TextType.BOLD),
				TextNode(" with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word and a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" and an ", TextType.TEXT),
				TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
				TextNode(" and a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
			],
			new_node,
		)


	def test_eq2(self):
		text = ("This is **text** with an _italic_ word "
			"and a `code block` "
			"and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
			"and a [link](https://boot.dev)")
		new_node = text_to_textnodes(text)
		self.assertEqual([
				TextNode("This is ", TextType.TEXT),
				TextNode("text", TextType.BOLD),
				TextNode(" with an ", TextType.TEXT),
				TextNode("italic", TextType.ITALIC),
				TextNode(" word and a ", TextType.TEXT),
				TextNode("code block", TextType.CODE),
				TextNode(" and an ", TextType.TEXT),
				TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
				TextNode(" and a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://boot.dev"),
			],
			new_node,
		)


	def test_text_to_textnodes_empty(self):
		nodes = text_to_textnodes("")
		self.assertEqual(len(nodes), 1)
		self.assertEqual(nodes[0].text, "")
		self.assertEqual(nodes[0].text_type, TextType.TEXT)

	def test_text_to_textnodes_plain_text(self):
		text = "Just plain text, no markdown"
		nodes = text_to_textnodes(text)
		self.assertEqual(len(nodes), 1)
		self.assertEqual(nodes[0].text, text)
		self.assertEqual(nodes[0].text_type, TextType.TEXT)

	def test_text_to_textnodes_adjacent_markdown(self):
		text = "**Bold**_italic_`code`"
		nodes = text_to_textnodes(text)
		self.assertEqual(len(nodes), 3)

