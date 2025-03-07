import unittest

from split_nodes import *
from extract_markdown_images import *

class TestSplitImagesLinks(unittest.TestCase):
	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
			"and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

	def test_split_links(self):
		node = TextNode(
			"This is text with a [link](https://i.imgur.com/zjjcJKZ.png) "
			"and another [second link](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a ", TextType.TEXT),
				TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)

	def test_split_no_image(self):
		node = TextNode(
			"This is a text without a link "
			"this also has no image",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertEqual([TextNode(
					"This is a text without a link "
					"this also has no image",
					TextType.TEXT,
				)], new_nodes)

	def test_split_wrong_text_type(self):
		node = TextNode(
			"This is a text with a link [link](https://i.imgur.com/zjjcJKZ.png) "
			"this also has no image",
			TextType.LINK,
		)
		new_nodes = split_nodes_link([node])
		self.assertEqual([TextNode(
					"This is a text with a link [link](https://i.imgur.com/zjjcJKZ.png) "
					"this also has no image",
					TextType.LINK,
				)], new_nodes)

	def test_split_image_begin(self):
		node = TextNode(
				"![image](https://i.imgur.com/zjjcJKZ.png) This image is at the beginning "
				"and at the end ![second image](https://i.imgur.com/3elNhQu.png)",
				TextType.TEXT,
			)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" This image is at the beginning and at the end ", TextType.TEXT),
				TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)
