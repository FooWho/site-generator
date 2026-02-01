from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        text_blocks = node.text.split(delimiter)
        if not len(text_blocks) % 2:
            raise Exception(f"No matching delimiter for {delimiter} in {node.text}!")
        for i in range(len(text_blocks)):
            if i % 2 == 0:
                block = TextNode(text_blocks[i], TextType.TEXT)
                new_nodes.append(block)
            else:
                block = TextNode(text_blocks[i], text_type)
                new_nodes.append(block)
    return new_nodes
            