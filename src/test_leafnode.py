import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="This is a link.", props={"href": "https://msn.com/", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://msn.com/" target="_blank">This is a link.</a>')

    def test_leaf_to_html_a2(self):
        node = LeafNode(tag="a", value="This is another link.", props={"href": "https://www.google.com/"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com/">This is another link.</a>')

    def test_leaf_to_html_p2(self):
        node = LeafNode("p", "Hello, world, yet again!")
        self.assertEqual(node.to_html(), "<p>Hello, world, yet again!</p>")

