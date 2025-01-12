import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, Bold text, None)")
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
        self.assertEqual(node, node2)
    def test_eq_url_false(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.yahoo.com")
        self.assertNotEqual(node, node2)
    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node", "invalid")


if __name__ == "__main__":
    unittest.main()