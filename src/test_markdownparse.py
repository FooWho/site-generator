import unittest

from textnode import TextNode, TextType
from markdownparse import split_nodes_delimiter

class TestMarkdownParse(unittest.TestCase):
    def test_markdown_bold(self):
        node = TextNode("This is some **bold** text!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is some ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text!", TextType.TEXT)])

    def test_markdown_plain(self):
        node = TextNode("This is some plain old text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is some plain old text.", TextType.TEXT)])

    def test_markdown_code(self):
        node = TextNode("This `is text` with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This ", TextType.TEXT), TextNode("is text", TextType.CODE), TextNode(" with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)])