import unittest
from htmlnode import LeafNode
from textnode import TextType

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_to_html_no_tag(self):
        node = LeafNode("This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None)
    
    def test_to_html_with_props(self):
        node = LeafNode("google.com", props={"href": "google.com"}, node_type=TextType.LINK)
        self.assertEqual(node.to_html(), '<a href="google.com">google.com</a>')

    def test_empty_string_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("")
    
    def test_special_char_in_value(self):
        node = LeafNode("This is a paragraph with a special character: &")
        self.assertEqual(node.to_html(), "This is a paragraph with a special character: &amp;")


if __name__ == "__main__":
    unittest.main()