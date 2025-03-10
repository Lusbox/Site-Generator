def extract_title(markdown):
	if markdown.startswith('#'):
		return markdown.strip('# ')
	else:
		raise Exception ("no header")
