from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Hyperlink"
    IMAGE = "Image"

class TextNode:
    
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