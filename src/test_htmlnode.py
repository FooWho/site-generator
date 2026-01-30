import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode1(self):
        node = HTMLNode(tag="a", value="This is a link.", props={"href": "https://boot.dev/", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://boot.dev/\" target=\"_blank\"")

    def test_htmlnode2(self):
        node = HTMLNode(tag="p", value="This is a paragraph.", props={"color": "red"})
        self.assertEqual(node.props_to_html(), " color=\"red\"")

    def test_htmlnode3(self):
        node = HTMLNode(tag="a", value="This is a link.", props={"href": "https://www.google.com/"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com/\"")

    def test_htmlnode4(self):
        node = HTMLNode(tag="a", value="This is a link.", props={"href": "https://msn.com/", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://msn.com/\" target=\"_blank\"")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_text_plain(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_image(self):
        node = TextNode("This is an image", TextType.IMAGE, url="http://www.images.com/myimage.jpg")
        html_node = text_node_to_html_node(node)
        if html_node.props is not None:
            self.assertEqual(html_node.props["src"], "http://www.images.com/myimage.jpg")
            self.assertEqual(html_node.props["alt"], "This is an image")
        else:
            self.assertEqual(True, False)

