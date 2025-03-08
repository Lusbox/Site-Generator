import unittest

from markdown_to_blocks import *

class TestMarkToBlock(unittest.TestCase):
	def test_markdown_to_blocks(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)

	def test_markdown_to_blocks2(self):
		md = """

This is `coded` paragraph


This is another paragraph with **bold** text and `code` here
This is the same paragraph on a new line
This is another new line with _italic_ text

- This is a list

- This is also a list
"""
		blocks = markdown_to_blocks(md)
		self.assertEqual(
			blocks,
			[
				"This is `coded` paragraph",
				"This is another paragraph with **bold** text and `code` here\nThis is the same paragraph on a new line\nThis is another new line with _italic_ text",
				"- This is a list",
				"- This is also a list"
			],
		)

