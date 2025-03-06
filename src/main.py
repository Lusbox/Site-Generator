from textnode import *

def main():
	test_object = TextNode("anchor_text", TextType.LINK, "https://www.boot.dev")
	print(repr(test_object))

main()
