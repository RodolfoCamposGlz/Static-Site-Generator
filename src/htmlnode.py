
class HTMLNode ():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
           raise ValueError()
        if self.tag is None:
            self.tag = ""
        props = self.props_to_html()
        if self.tag == "":
            return f"{self.value}"
        else:
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is not defined")
        props = self.props_to_html()
        children_html = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}{props}>{children_html}</{self.tag}>"
    
