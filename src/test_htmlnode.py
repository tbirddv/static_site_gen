import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(repr(node), "HTMLNode(Tag = p, Value = This is a paragraph, Children = None)")
    
    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode("p", "This is a paragraph")
            node.to_html()

if __name__ == "__main__":
    unittest.main()