class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception("Not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        value = ""
        for prop in self.props:
            value += f' {prop}="{self.props[prop]}"'
        return value


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"