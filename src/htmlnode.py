from html import escape as html_escape
from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            return "".join([f' {key}="{value}"' for key, value in self.props.items()])
        return ""
    
    def __repr__(self):
        return f"HTMLNode(Tag = {self.tag}, Value = {self.value}, Children = {self.children})"

class ImageNode(HTMLNode):
    def __init__(self, src, alt):
        if not src or not alt:
            raise ValueError("Images require a source and alt text")
        self.tag = "img"
        self.props = {"src":src, "alt":html_escape(alt, quote=True)}


    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>"
    
class LinkNode(HTMLNode):
    def __init__(self, value, url, title=None):
        if not value or not url:
            raise ValueError("Hyperlinks require a url and link text")
        self.tag = "a"
        self.value = html_escape(value, quote=True)
        if title:
            self.props = {"href":url, "title":html_escape(title, quote=True)}
        else:
            self.props = {"href":url}

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, value, node_type=TextType.NORMAL):
        if not value:
            raise ValueError("Leaf node must have a value")
        self.value = html_escape(value, quote=True)
        self.text_type = node_type
        leaf_type = TextNode(node_type)
        self.tag = leaf_type.get_tag()


    def to_html(self):
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return self.value
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Parent node must have a tag")
        if not children:
            raise ValueError("Parent node must have child nodes")
        super().__init__(tag, None, children)
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node requires a tag.")
        if not self.children:
            raise ValueError("Parent node must have children.")

        # Preprocess by wrapping "Normal Text" (tag=None) in <p>
        for child in self.children:
            if isinstance(child, LeafNode) and child.tag is None:
                # If the parent tag is not <p>, wrap the Normal Text in "<p>"
                if self.tag != "p":
                    child.tag = "p"

        # Render all children and parent tags as normal
        children_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"