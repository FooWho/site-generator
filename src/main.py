from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    myTextNode = TextNode("Hi!", TextType.PLAIN)
    print(myTextNode)
    myLeafNode = LeafNode(tag="a", value="This is a link.", props={"href": "https://msn.com/", "target": "_blank"})
    print(myLeafNode)
    print(myLeafNode.to_html())

main()

