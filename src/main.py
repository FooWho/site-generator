from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from textnode import TextNode, TextType


def main():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())

    myTextNode = TextNode("This is a test.", TextType.TEXT)
    myLeafNode = text_node_to_html_node(myTextNode)
    print(myLeafNode)


main()

