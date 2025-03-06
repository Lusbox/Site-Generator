class HTMLNode:
	def __init__ (self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if not self.props:
			return ""
		props_str = ""
		for key, value in self.props.items():
			props_str += f' {key}="{value}"'
		return props_str

	def __repr__(self):
		print(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}")




class LeafNode(HTMLNode):
	def __init__ (self, tag, value, props=None):
		super().__init__()
		self.tag = tag
		self.value = value
		self.props = props

	def to_html(self):
		if self.value is None:
			raise ValueError
		if self.tag is None:
			return self.value
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
	def __init__ (self, tag, children, props=None):
		super().__init__()
		self.tag = tag
		self.children = children
		self.props = props

	def to_html(self):
		if not self.children:
			raise ValueError
		if not all(isinstance(child, HTMLNode) for child in self.children):
			raise TypeError ("All children must be instances of HTMLNode")
		if self.tag is None:
			raise ValueError ("missing tag")
		if self.children is None:
			raise ValueError ("missing children")
		html_str = ""
		for child in self.children:
			html_str += child.to_html()
		return f"<{self.tag}>{html_str}</{self.tag}>"
