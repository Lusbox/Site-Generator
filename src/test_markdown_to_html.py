import unittest

from htmlnode import *
from markdown_to_html import *

class TestMarkdownHTML(unittest.TestCase):
	def test_paragraphs(self):
		md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)

	def test_codeblock(self):
		md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)

	def test_heading(self):
		md = """
# This text is a heading with **bolded** text

## And some _italic_ text
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><h1>This text is a heading with <b>bolded</b> text</h1><h2>And some <i>italic</i> text</h2></div>",
		)

	def test_ordered_list(self):
		md = """
1. This is my
2. amazingly
3. ordered list
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
				html,
				"<div><ol><li>This is my</li><li>amazingly</li><li>ordered list</li></ol></div>"
		)

	def test_unordered_list(self):
		md = """
- stay ordered
- my list won't
- help
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><ul><li>stay ordered</li><li>my list won't</li><li>help</li></ul></div>"
		)

