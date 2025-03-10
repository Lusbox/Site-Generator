import sys

from textnode import *
from copy_dir import *
from generate_pages import *

def main():
	test_object = TextNode("anchor_text", TextType.LINK, "https://www.boot.dev")
	print(repr(test_object))

basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
print(f"Using basepath: {basepath}")

main()
copy_to_dir("static", "docs")

generate_pages_recursive("content", "template.html", "docs", basepath)
