from split_node import split_node_delimiter
from htmlnode import LeafNode, LinkNode, BaseNode
from textnode import TextNode, TextType



print(split_node_delimiter(BaseNode('[text](url "title")', TextType.NORMAL), "[", TextType.LINK))