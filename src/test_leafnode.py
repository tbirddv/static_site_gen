import unittest
from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_props(self):
        node = LeafNode("a", "google.com", props={"href": "google.com"})
        self.assertEqual(node.to_html(), '<a href="google.com">google.com</a>')