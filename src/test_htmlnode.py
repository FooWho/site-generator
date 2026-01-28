import unittest

from htmlnode import HTMLNode

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