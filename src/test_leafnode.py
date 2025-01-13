import unittest
from htmlnode import LeafNode, LinkNode, ImageNode
from textnode import TextType

class TestLeafNode(unittest.TestCase):

    def test_to_html_bold(self):
        node = LeafNode("This is a bold paragraph", node_type=TextType.BOLD)
        self.assertEqual(node.to_html(), "<b>This is a bold paragraph</b>")

    def test_to_html_no_tag(self):
        node = LeafNode("This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None)
    
    def test_LinkNode_to_html(self):
        node = LinkNode("google.com", "google.com")
        self.assertEqual(node.to_html(), '<a href="google.com">google.com</a>')

    def test_link_node_with_title(self):
        node = LinkNode("Click here", "google.com", "Visit Google")
        self.assertEqual(node.to_html(), '<a href="google.com" title="Visit Google">Click here</a>')

    def test_empty_string_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("")
    
    def test_special_char_in_value(self):
        node = LeafNode("This is a paragraph with a special character: &")
        self.assertEqual(node.to_html(), "This is a paragraph with a special character: &amp;")

    def test_link_node_invalid_input(self):
        with self.assertRaises(ValueError):
            node = LinkNode("", "google.com")
        with self.assertRaises(ValueError):
            node = LinkNode("Click", "")

    def test_image_node_valid(self):
        node = ImageNode("test.jpg", "Test image")
        self.assertEqual(node.to_html(), '<img src="test.jpg" alt="Test image">')
    
    def test_image_node_special_chars(self):
        node = ImageNode("test.jpg", "Test & image")
        self.assertEqual(node.to_html(), '<img src="test.jpg" alt="Test &amp; image">')
    
    def test_image_node_invalid_input(self):
        with self.assertRaises(ValueError):
            node = ImageNode("", "alt text")
        with self.assertRaises(ValueError):
            node = ImageNode("test.jpg", "")

    def test_leaf_node_code(self):
        node = LeafNode("Code block", node_type=TextType.CODE)
        self.assertEqual(node.to_html(), "<code>Code block</code>")

    def test_leaf_node_italic(self):
        node = LeafNode("italic text", node_type=TextType.ITALIC)
        self.assertEqual(node.to_html(), "<i>italic text</i>")

    def test_link_node_preserves_url(self):
        url = "https://example.com?name=john&age=25"
        node = LinkNode("Click & learn", url)  # Note: text contains &
        expected = '<a href="https://example.com?name=john&age=25">Click &amp; learn</a>'
        # URL should remain unchanged, but link text should be escaped
        self.assertEqual(node.to_html(), expected)

    def test_image_node_preserves_src(self):
        src = "https://example.com/image.jpg?width=800&height=600"
        node = ImageNode(src, "Image & caption")  # Note: alt contains &
        expected = '<img src="https://example.com/image.jpg?width=800&height=600" alt="Image &amp; caption">'
        # URL should remain unchanged, but alt text should be escaped
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()