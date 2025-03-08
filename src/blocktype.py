import re
from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
	lines = markdown_block.split('\n')

	if re.match(r"^(#{1,6} )(.*?)", markdown_block):
		return BlockType.HEADING

	if re.match(r"^```.*```$", markdown_block, re.DOTALL):
		return BlockType.CODE

	if all(line.startswith('>') for line in lines):
		return BlockType.QUOTE

	if all(line.startswith('- ') for line in lines):
		return BlockType.UNORDERED_LIST

	is_ordered_list = True
	for i, line in enumerate(lines):
		expected_prefix = f"{i+1}. "
		if not line.startswith(expected_prefix):
			is_ordered_list = False
			break

	if is_ordered_list and lines:
		return BlockType.ORDERED_LIST

	return BlockType.PARAGRAPH
