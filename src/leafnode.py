from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super(LeafNode, self).__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        return_string = f'<{self.tag}'
        if self.props is not None:
            return_string = return_string + self.props_to_html()
        return_string = return_string + f'>{self.value}</{self.tag}>'
        return return_string
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"