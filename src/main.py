from textnode import TextNode, TextType

def main():
    test1 = TextNode("Hello", TextType.NORMAL)
    test2 = TextNode("I'M BOLD", TextType.BOLD)
    test3 = TextNode("I'm italic", TextType.ITALIC)
    test4 = TextNode("I'm code", TextType.CODE)
    test5 = TextNode("I'm a link", TextType.LINK, "https://www.google.com")
    test6 = TextNode("I'm an image", TextType.IMAGE, "https://www.google.com")
    test7 = TextNode("I'm an image", TextType.IMAGE, "https://www.google.com")

    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)
    print(test6)
    print(test7)

    print(test1 == test2)
    print(test6 == test7)

if __name__ == "__main__":
    main()