from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdownparse import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image, text_to_textnodes, markdown_to_blocks, block_to_block_type, markdown_to_html_node
from sitecreator import copy_source_to_dest, extract_title, generate_page, generate_pages_recursive

def main():
    """
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

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    """
    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com)"
    #print(extract_markdown_links(text))
    
    """
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    #node = TextNode("[to bootdev](https://www.boot.dev)[to youtube](https://www.youtube.com/@bootdev)", TextType.TEXT)
    nodes = [node]
    new_nodes = split_nodes_link(nodes)
    print(new_nodes)
    

    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    nodes = [node]
    new_nodes = split_nodes_image(nodes)
    print(new_nodes)
    
    #node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)
    #nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    #print(nodes)
    """

    #md = """
#This is text that _should_ remain
#the **same** even with inline stuff. It has a [link to youtube.](https://www.youtube.com/)
#"""


    #parent_document = markdown_to_html_node(md)
    #print(f"{parent_document}")

    copy_source_to_dest("static", "public")
    generate_pages_recursive("content", "template.html", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    #generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    #generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    #generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    #generate_page("content/contact/index.md", "template.html", "public/contact/index.html")
    


main()

