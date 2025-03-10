from textnode import *
from copy_dir import *
from generate_pages import *

def main():
	test_object = TextNode("anchor_text", TextType.LINK, "https://www.boot.dev")
	print(repr(test_object))

main()
copy_to_dir()

generate_pages_recursive("content", "template.html", "public")
