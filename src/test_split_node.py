import unittest
from html import escape as html_escape
from htmlnode import LeafNode, LinkNode, ImageNode, BaseNode
from textnode import TextType
from split_node import split_node_delimiter

class test_split_node(unittest.TestCase):
    def test_simple_italic(self):
        node = BaseNode("This is a paragraph with *italic text* for testing")
        result = split_node_delimiter(node, "*", TextType.ITALIC)
        expected = [BaseNode("This is a paragraph with ", TextType.NORMAL), BaseNode("italic text", TextType.ITALIC), BaseNode(" for testing", TextType.NORMAL)]
        self.assertEqual(result, expected)
    
    def test_simple_bold(self):
        node = BaseNode("This is a paragraph with **bold text** for testing")
        result = split_node_delimiter(node, "**", TextType.BOLD)
        expected = [BaseNode("This is a paragraph with ", TextType.NORMAL), BaseNode("bold text", TextType.BOLD), BaseNode(" for testing", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_simple_code(self):
        node = BaseNode("This is a paragraph with `print('Hello World!')` for testing")
        result = split_node_delimiter(node, "`", TextType.CODE)
        expected = [BaseNode("This is a paragraph with ", TextType.NORMAL), BaseNode("print('Hello World!')", TextType.CODE), BaseNode(" for testing", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_bold_nested_italic(self):
        node = BaseNode("This is bold text with some *nested italic text* for testing", TextType.BOLD)
        result = split_node_delimiter(node, "*", TextType.ITALIC)
        expected = [BaseNode("This is bold text with some ", TextType.BOLD), BaseNode("nested italic text", TextType.ITALIC), BaseNode(" for testing", TextType.BOLD)]
        self.assertEqual(result, expected)

    def test_keep_raw_delimiter(self):
        node = BaseNode("Text **** more", TextType.NORMAL)
        new_nodes = split_node_delimiter(node, "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [BaseNode("Text **"), BaseNode("** more")])

    def test_multiple_delimiter_pairs_and_ending_delimiter(self):
        node = BaseNode("Text **bold** more **bold2**", TextType.NORMAL)
        new_nodes = split_node_delimiter(node, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [BaseNode("Text "), BaseNode("bold", TextType.BOLD), BaseNode(" more "), BaseNode("bold2", TextType.BOLD)])

    def test_missing_delimiter(self):
        with self.assertRaises(Exception):
            node = BaseNode("Text **bold", TextType.NORMAL)
            split_node_delimiter(node, "**", TextType.BOLD)

    def test_raw_delimiter_and_inline(self):
        node = BaseNode("Text **** more ** bold **")
        result = split_node_delimiter(node, "**", TextType.BOLD)
        expected = [BaseNode("Text ****"), BaseNode(" more "), BaseNode(" bold ", TextType.BOLD)]
        self.assertEqual(result, expected)

    def test_keep_raw_delimiter_at_end(self):
        node = BaseNode("Text ****", TextType.NORMAL)
        new_nodes = split_node_delimiter(node, "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [BaseNode("Text **"), BaseNode("**")])

    def test_keep_raw_delimiter_at_beginning(self):
        node = BaseNode("**** more", TextType.NORMAL)
        new_nodes = split_node_delimiter(node, "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [BaseNode("**"), BaseNode("** more")])

    def test_link_no_title(self):
        node = BaseNode("This is a paragraph of text with an [Example.com](Example.com) Link")
        result = split_node_delimiter(node, "[", TextType.LINK)
        expected = [BaseNode("This is a paragraph of text with an "), LinkNode("Example.com", "Example.com"), BaseNode(" Link")]
        self.assertEqual(result, expected)

    def test_link_with_title_at_end(self):
        node = BaseNode('This is a paragraph of text with a [Link](Example.com "This is a Link!")')
        result = split_node_delimiter(node, "[", TextType.LINK)
        expected = [BaseNode("This is a paragraph of text with a "), LinkNode("Link", "Example.com ", "This is a Link!")]
        self.assertEqual(result, expected)

    def test_empty_bracket(self):
        node = BaseNode("This is a paragraph of text with empty [](brackets)")
        result = split_node_delimiter(node, "[", TextType.LINK)
        expected = [node]
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()