import unittest
from htmlnode import ParentNode, HTMLNode, LeafNode, LinkNode, ImageNode
from textnode import TextType, TextNode

class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        node1 = LeafNode("Hello, World!")
        node2 = LeafNode("Goodbye, World!")
        parent = ParentNode("div", [node1, node2])
        self.assertEqual(parent.to_html(), '<div><p>Hello, World!</p><p>Goodbye, World!</p></div>')

    def test_parentnode_error(self):
        node1 = LeafNode("Hello, World!")
        with self.assertRaises(ValueError):
            parent = ParentNode(None, [node1])
            parent.to_html()
    
    def test_no_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("div", [])
            parent.to_html()

    def test_all_text_types(self):
        node1 = LeafNode("Hello, World!")
        node2 = LeafNode("Goodbye, World!", node_type=TextType.BOLD)
        node3 = LeafNode("Goodbye, World!", node_type=TextType.ITALIC)
        node4 = LeafNode("print('Hello, World!')", node_type=TextType.CODE)
        node5 = LinkNode("Click me!", "https://www.example.com")
        node6 = ImageNode("Test.jpg", "Test Image")
        parent = ParentNode("p", [node1, node2, node3, node4, node5, node6])
        self.assertEqual(parent.to_html(), ('<p>Hello, World!'
                                            '<b>Goodbye, World!</b>'
                                            '<i>Goodbye, World!</i>'
                                            '<code>print(&#x27;Hello, World!&#x27;)</code>'
                                            '<a href="https://www.example.com">Click me!</a>'
                                            '<img src="Test.jpg" alt="Test Image"></p>'))

    def test_nested_parent_nodes(self):
        node1 = LeafNode("Hello, World!")
        node2 = LeafNode("Goodbye, World!")
        parent1 = ParentNode("div", [node1, node2])
        parent2 = ParentNode("section", [parent1])
        self.assertEqual(parent2.to_html(), '<section><div><p>Hello, World!</p><p>Goodbye, World!</p></div></section>')

    def test_complex_html_structure(self):
        # Build the complex nested structure
        node = ParentNode(
            "div",
            [
                LeafNode("Bold text", node_type=TextType.BOLD),
                LeafNode("Just some normal text"),
                ParentNode(
                    "section",
                    [
                        LeafNode("Italic text", node_type=TextType.ITALIC),
                        LeafNode("More normal text"),
                    ],
                ),
                LeafNode("Final bit of untagged text"),
            ],
        )

        # Generate HTML
        result = node.to_html()

        # Expected HTML output
        expected =("<div><b>Bold text</b>"
                   "<p>Just some normal text</p>"
                   "<section><i>Italic text</i>"
                   "<p>More normal text</p>"
                   "</section><p>Final bit of untagged text</p></div>")

        # Assert the generated HTML matches the expected output
        self.assertEqual(result, expected)

    def test_parent_node_with_props(self):
        node = LeafNode("Hello, World!")
        parent = ParentNode("div", [node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><p>Hello, World!</p></div>'
            )

if __name__ == "__main__":
    unittest.main()