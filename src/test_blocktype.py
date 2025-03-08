import unittest

from blocktype import *

class TestBlockType(unittest.TestCase):
	def test_1(self):
		markdown_block = "# This is a heading"
		self.assertEqual(BlockType.HEADING, block_to_block_type(markdown_block))

	def test_2(self):
		markdown_block = "```I am code```"
		self.assertEqual(BlockType.CODE, block_to_block_type(markdown_block))

	def test_3(self):
		markdown_block = """> I am a quote block
> I am also a quote block"""
		self.assertEqual(BlockType.QUOTE, block_to_block_type(markdown_block))

	def test_4(self):
		markdown_block = """- I am entirely
- unordered"""
		self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(markdown_block))

	def test_5(self):
		markdown_block = """1. I am entirely
2. an ordered
3. list"""
		self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(markdown_block))

	def test_6(self):
		markdown_block = "I am just a lowly paragraph"
		self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(markdown_block))

	def test_multiple_heads(self):
		markdown_block = "#### This is a heading"
		self.assertEqual(BlockType.HEADING, block_to_block_type(markdown_block))

	def test_multi_code(self):
		markdown_block = """``` This is a mega
huge code block```"""
		self.assertEqual(BlockType.CODE, block_to_block_type(markdown_block))

	def test_empty_para(self):
		markdown_block = ""
		self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(markdown_block))

	def test_not_heading(self):
		markdown_block = "#This is not? a heading"
		self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(markdown_block))

	def test_not_quote(self):
		markdown_block = """> Look ma
I'm a quote block"""
		self.assertNotEqual(BlockType.QUOTE, block_to_block_type(markdown_block))
