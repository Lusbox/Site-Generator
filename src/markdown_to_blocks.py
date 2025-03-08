def markdown_to_blocks(markdown):
	block_list = []
	blocks = markdown.split('\n\n')

	for block in blocks:
		strip_block = block.strip()
		if strip_block:
			block_list.append(strip_block)

	return block_list
