class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method is not yet implemented.")
    
    def props_to_html(self):
        html_string = ""
        if self.props is None:
            return html_string
        for property in self.props:
            html_string += f' {property}="{self.props[property]}"'
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None:
            self.children = []
        super(ParentNode, self).__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required.")
        if self.children is None:
            raise ValueError("ParentNode has no children!")
        html_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html_string += child.to_html()
        html_string += f'</{self.tag}>'
        return html_string
    
    def add_child(self, child_node):
        if self.children is None:
            self.children = [child_node]
        else:
            self.children.append(child_node)


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
    

        
