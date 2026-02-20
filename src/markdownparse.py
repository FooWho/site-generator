from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_blocks = node.text.split(delimiter)
        if not len(text_blocks) % 2:
            raise Exception(f"No matching delimiter for {delimiter} in {node.text}!")
        for i in range(len(text_blocks)):
            if i % 2:
                block = TextNode(text_blocks[i], text_type)
                new_nodes.append(block)
            else:
                block = TextNode(text_blocks[i], TextType.TEXT)
                new_nodes.append(block)
                
    return new_nodes

def extract_markdown_images(text):
    #![alt text](image.jpg)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    #[title](url)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    node_list = []
    start_node = TextNode(text, TextType.TEXT)
    node_list = split_nodes_link([start_node])
    node_list = split_nodes_image(node_list)
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
    return node_list

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    processed = []
    for block in blocks:
        if block != "":
            block = block.strip()
            processed.append(block)
    return processed

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    parent_doc = ParentNode("div", None)
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.HEADING:
                leaf = parse_heading(block)
                if leaf.tag != "h1":
                    parent_doc.add_child(leaf)
            case BlockType.PARAGRAPH:
                p_parent = parse_paragraph(block)
                parent_doc.add_child(p_parent)
            case BlockType.CODE:
                pre_parent = ParentNode("pre", None)
                leaf = parse_code(block)
                pre_parent.add_child(leaf)
                parent_doc.add_child(pre_parent)
    #print(f"{parent_doc.to_html()}")
    return parent_doc



def parse_paragraph(block): 
    p_parent = ParentNode("p", None)
    block = block.replace("\n", " ")
    nodes = text_to_textnodes(block)
    for node in nodes:
        node = text_node_to_html_node(node)
        p_parent.add_child(node)
    return p_parent

def parse_heading(block):
    if block.startswith("# "):
        block = block.replace("# ", "")
        block = block.strip()
        leaf = LeafNode("h1", block)
    if block.startswith("## "):
        block = block.replace("## ", "")
        block = block.strip()
        leaf = LeafNode("h2", block)
    if block.startswith("### "):
        block = block.replace("### ", "")
        block = block.strip()
        leaf = LeafNode("h3", block)
    if block.startswith("#### "):
        block = block.replace("#### ", "")
        block = block.strip()
        leaf = LeafNode("h4", block)
    if block.startswith("##### "):
        block = block.replace("##### ", "")
        block = block.strip()
        leaf = LeafNode("h5", block)
    if block.startswith("###### "):
        block = block.replace("## ", "")
        block = block.strip()
        leaf = LeafNode("h6", block)
    return leaf

def parse_code(block):
    block = block.replace("```", "")
    block = block.strip()
    block += "\n"
    leaf = LeafNode("code", block)
    return leaf