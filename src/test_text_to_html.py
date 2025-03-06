import unittest

from text_to_html import *

class TestTextHTML(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_text2(self):
		node = TextNode("This is a text node", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is a text node")

	def test_text3(self):
		node = TextNode("This is a text node", TextType.LINK, "http://www.google.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "This is a text node")
		self.assertEqual(html_node.props, {'href': 'http://www.google.com'})

	def test_text4(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is a text node")

	def test_text5(self):
		node = TextNode("This is a text node", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "This is a text node")

	def test_text6(self):
		node = TextNode("image text", TextType.IMAGE, "http://www.google.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {'src': 'http://www.google.com', 'alt': 'image text'})
