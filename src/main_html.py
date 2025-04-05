from textnode import *
from htmlnode import *

def main():
    
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    ans = parent_node.to_html()
    print(ans)

main()
