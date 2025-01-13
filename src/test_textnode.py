import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode("invalid")


if __name__ == "__main__":
    unittest.main()