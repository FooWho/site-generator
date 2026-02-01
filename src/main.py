from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from textnode import TextNode, TextType
from markdownparse import split_nodes_delimiter


def main():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())

    myTextNode = TextNode("This is a test.", TextType.TEXT)
    myLeafNode = text_node_to_html_node(myTextNode)
    print(myLeafNode)

    node = TextNode("This `is text` with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

    node = TextNode("This is some **bold** text!", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)

main()

