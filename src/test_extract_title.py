import unittest

from extract_title import *

class TestTitle(unittest.TestCase):
	def test_1(self):
		markdown = "# Hello"
		self.assertEqual("Hello", extract_title(markdown))
