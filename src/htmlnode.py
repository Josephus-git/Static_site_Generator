

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        ans = ""
        for key, value in self.props.items():
            ans += f' {key}="{value}"'
        return ans
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        elif self.props != None:
            ans = f"<{self.tag}{self.props_to_html()}>Click me!</{self.tag}>"
            return ans
        else:
            ans = f"<{self.tag}>{self.value}</{self.tag}>"
            return ans
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        def rec_child(list_child):
                if type(list_child) != list:
                    return
                
                for i in list_child:
                    rec_child(i.to_html())
                    return i.to_html()

        if self.tag == None:
            raise ValueError("All parent node must have a tag")
        elif self.children == None:
            raise ValueError("All parent node must have children")
        
        else:
            ans = f"<{self.tag}>{rec_child(self.children)}</{self.tag}>"
            return ans

        
        
