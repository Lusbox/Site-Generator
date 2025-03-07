import unittest

from split_nodes import *

class TestSplitNode(unittest.TestCase):
	def test_eq_code(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_node = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(new_node, [
						TextNode("This is text with a ", TextType.TEXT),
						TextNode("code block", TextType.CODE),
						TextNode(" word", TextType.TEXT),
					])

	def test_eq_bold(self):
		node = TextNode("This is text with a **code block** word", TextType.TEXT)
		new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertEqual(new_node, [
						TextNode("This is text with a ", TextType.TEXT),
						TextNode("code block", TextType.BOLD),
						TextNode(" word", TextType.TEXT),
					])

	def test_eq_syntax(self):
		node = TextNode("This is text with a `code block word", TextType.TEXT)
		with self.assertRaises(Exception) as context:
			split_nodes_delimiter([node], "`", TextType.CODE)

	def test_eq_multiple(self):
		node = TextNode("This is text with a _code block_ word and so is _this_", TextType.TEXT)
		new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertEqual(new_node, [
						TextNode("This is text with a ", TextType.TEXT),
						TextNode("code block", TextType.ITALIC),
						TextNode(" word and so is ", TextType.TEXT),
						TextNode("this", TextType.ITALIC)
					])
