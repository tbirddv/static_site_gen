from textnode import TextType
from htmlnode import LeafNode, LinkNode, ImageNode, BaseNode

def has_link_pattern_before_next_bracket(text):
    link_pattern_index = text.find("](")
    next_bracket_index = text.find("[")
    
    # If there's no next bracket, just check if link pattern exists
    if next_bracket_index == -1:
        return link_pattern_index != -1
        
    # If there's no link pattern, return False
    if link_pattern_index == -1:
        return False
        
    # Return True if link pattern comes before next bracket
    return link_pattern_index < next_bracket_index

def split_node_delimiter(oldnode, delimiter, text_type):
    #Returns a list of BaseNode and LinkNodes as applicable, oldnode should be a BaseNode
    try:
        if text_type == TextType.LINK:
            new_values = oldnode.value.split("[", 1)
            if len(new_values) == 1:
                return [oldnode]
            if not has_link_pattern_before_next_bracket(new_values[1]):
                return [BaseNode(new_values[0] + "[", oldnode.text_type)] + split_node_delimiter(BaseNode(new_values[1], oldnode.text_type), delimiter, text_type)
            new_values = [new_values[0]] + new_values[1].split("]", 1)
            if len(new_values) == 2:
                raise Exception("Missing a delimiter")
            if not new_values[2].startswith("("):
                raise Exception("Missing opening parenthesis in link")
            new_values = new_values[:2] + new_values[2][1:].split(")", 1)
            #new_values = before_text, link_text, url, after_text
            if len(new_values) == 3:
                raise Exception("Missing closing parenthesis in link")
            if not new_values[1] or not new_values[2]:
                if "[" in new_values[3]:
                    return [BaseNode("".join(new_values[:3]), oldnode.text_type)] + split_node_delimiter(BaseNode(new_values[3], oldnode.text_type), delimiter, text_type)
                return [oldnode]
            if '"' in new_values[2]:
                new_values = new_values[:2] + new_values[2].split('"',2)[:2] + [new_values[3]]
                #new_values = before_text, link_text, url, title, after_text
                if new_values[4]:
                    if "[" in new_values[4]:
                        return [BaseNode(new_values[0], oldnode.text_type), LinkNode(new_values[1], new_values[2], new_values[3])] + split_node_delimiter(BaseNode(new_values[4], oldnode.text_type), delimiter, text_type)
                    return [BaseNode(new_values[0], oldnode.text_type), LinkNode(new_values[1], new_values[2], new_values[3]), BaseNode(new_values[4], oldnode.text_type)]
                return [BaseNode(new_values[0], oldnode.text_type), LinkNode(new_values[1], new_values[2], new_values[3])]
            if new_values[3]:
                if "[" in new_values[3]:
                    return [BaseNode(new_values[0], oldnode.text_type), LinkNode(new_values[1], new_values[2])] + split_node_delimiter(BaseNode(new_values[3], oldnode.text_type), delimiter, text_type)
                return [BaseNode(new_values[0], oldnode.text_type), LinkNode(new_values[1], new_values[2]), BaseNode(new_values[3], oldnode.text_type)]
            return [BaseNode(new_values[0], oldnode.text_type), LinkNode(new_values[1], new_values[2])]
                    
        new_values = oldnode.value.split(delimiter, 2)
        if len(new_values) == 1:
            return [BaseNode(oldnode.value, oldnode.text_type)]
        if len(new_values) == 2:
            raise Exception("Missing a delimiter")
        if not new_values[1]:
            if delimiter in new_values[2]:
                return [BaseNode(f"{new_values[0]}{delimiter}{delimiter}", oldnode.text_type)] + split_node_delimiter(BaseNode(new_values[2], oldnode.text_type), delimiter, text_type)
            return [oldnode]
        if new_values[2]:
            if delimiter in new_values[2]:
                return [BaseNode(new_values[0], oldnode.text_type), BaseNode(new_values[1], text_type)] + split_node_delimiter(BaseNode(new_values[2], oldnode.text_type), delimiter, text_type)       
            return [BaseNode(new_values[0], oldnode.text_type), BaseNode(new_values[1], text_type), BaseNode(new_values[2], oldnode.text_type)]
        return [BaseNode(new_values[0], oldnode.text_type), BaseNode(new_values[1], text_type)]
    except ValueError:
        if text_type == TextType.LINK:
            new_values = oldnode.value.split("[", 1)
            new_values = [new_values[0]] + new_values[1].split("]", 1)
            new_values = new_values[:2] + new_values[2][1:].split(")", 1)
            #new_values = before_text, link_text, url, after_text
            if '"' in new_values[2]:
                new_values = new_values[:2] + new_values[2].split('"',2)[:2] + [new_values[3]]
                #new_values = before_text, link_text, url, title, after_text
                if new_values[4]:
                    if "[" in new_values[4]:
                        return [LinkNode(new_values[1], new_values[2], new_values[3])] + split_node_delimiter(BaseNode(new_values[4], oldnode.text_type), delimiter, text_type)
                    return [LinkNode(new_values[1], new_values[2], new_values[3]), BaseNode(new_values[4], oldnode.text_type)]
                return [LinkNode(new_values[1], new_values[2], new_values[3])]
            if new_values[3]:
                if "[" in new_values[3]:
                    return [LinkNode(new_values[1], new_values[2])] + split_node_delimiter(BaseNode(new_values[3], oldnode.text_type), delimiter, text_type)
                return [LinkNode(new_values[1], new_values[2]), BaseNode(new_values[3], oldnode.text_type)]
            return [LinkNode(new_values[1], new_values[2])]
                    
        new_values = oldnode.value.split(delimiter, 2)
        if new_values[2]:
            if delimiter in new_values[2]:
                return [BaseNode(new_values[0], oldnode.text_type), BaseNode(new_values[1], text_type)] + split_node_delimiter(BaseNode(new_values[2], oldnode.text_type), delimiter, text_type)       
            return [BaseNode(new_values[0], oldnode.text_type), BaseNode(new_values[1], text_type), BaseNode(new_values[2], oldnode.text_type)]
        return [BaseNode(new_values[0], oldnode.text_type), BaseNode(new_values[1], text_type)]