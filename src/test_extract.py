import unittest

from extract_markdown_images import *

class TestExtract(unittest.TestCase):
	def test_eq(self):
		text = ("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
			"and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
		self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
								 ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])


	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
				"This is text with an link [to boot dev](https://www.boot.dev) "
				"and [to youtube](https://www.youtube.com/@bootdotdev)"
		)
		self.assertListEqual(
				[("to boot dev", "https://www.boot.dev"),
				("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
