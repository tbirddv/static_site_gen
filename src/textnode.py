from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Hyperlink"
    IMAGE = "Image"

class TextNode:
    ALLOWED_ATTRIBUTES = {
    TextType.NORMAL: [],
    TextType.BOLD: [],
    TextType.ITALIC: [],
    TextType.CODE: [],
    TextType.LINK: ["href", "title"],
    TextType.IMAGE: ["src", "alt"],
    }
    
    TAGS_BY_TEXT_TYPE = {
    TextType.NORMAL: None,
    TextType.BOLD: "b",
    TextType.ITALIC: "i",
    TextType.CODE: "code",
    TextType.LINK: "a",
    TextType.IMAGE: "img"
    }
    
    def __init__(self, text_type):
        if not isinstance(text_type, TextType):
            raise ValueError(f"text_type must be a TextType enum member, got '{text_type}'")
        self.text_type = text_type

    def get_tag(self):
        return self.TAGS_BY_TEXT_TYPE.get(self.text_type)
    
    def filter_props(self, props):
        allowed_keys = self.ALLOWED_ATTRIBUTES.get(self.text_type, [])
        return {key:value for key, value in props.items() if key in allowed_keys}

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"