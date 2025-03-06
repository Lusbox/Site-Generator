import unittest

from  htmlnode import *

class TestHTMLNode(unittest.TestCase):
	def test_eq(self):
		test_dict = {
				"href": "http://www.google.com",
				"target": "_blank",
			}
		node = HTMLNode("a", "4", None, test_dict)
		self.assertEqual(node.props_to_html(), ' href="http://www.google.com" target="_blank"')


	def test_eq2(self):
		test_dict = {
				"href": "http://www.google.com",
				"target": None,
			}
		node = HTMLNode("a", "4", None, test_dict)
		self.assertNotEqual(node.props_to_html(), ' href="http://www.google.com" target="_blank"')


	def test_eq3(self):
		test_dict = {
				"href": "http://www.google.com",
				"target": "_blank",
			}
		node = HTMLNode("a", "4", None, test_dict)
		self.assertNotEqual(node.props_to_html(), ' href="http://www.doogle.com" target="_blank"')


	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_p_with_attributes(self):
		test_dict = {
				"href": "http://www.google.com",
				"target": "_blank",
			}
		node = LeafNode("a", "Hello, world!", test_dict )
		self.assertEqual(node.to_html(), '<a href="http://www.google.com" target="_blank">Hello, world!</a>')

	def test_leaf_to_html_p_raise_value_error(self):
		test_dict = {
				"href": "http://www.google.com",
				"target": "_blank",
			}
		node = LeafNode("a", None, test_dict )
		self.assertRaises(ValueError, node.to_html)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

	def test_to_html_with_grandgrandchildren(self):
		grandgrandchild_node = LeafNode("a", None)
		grandchild_node = ParentNode("b", [grandgrandchild_node])
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertRaises(ValueError, parent_node.to_html)

	def test_to_html_without_tag(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode(None, [child_node])
		self.assertRaises(ValueError, parent_node.to_html)

	def test_to_html_without_children(self):
		parent_node = ParentNode("a", None)
		self.assertRaises(ValueError, parent_node.to_html)

	def test_to_html_empty_children(self):
		parent_node = ParentNode("a", [])
		self.assertRaises(ValueError, parent_node.to_html)

	def test_to_html_input_error_children(self):
		parent_node = ParentNode("a", ["user error input"])
		self.assertRaises(TypeError, parent_node.to_html)
