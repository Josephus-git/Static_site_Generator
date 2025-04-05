from textnode import *
from htmlnode import *

def main():
    
    new_obj = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    new_obj2 = LeafNode("p", "This is a paragraph of text.")
    ans = new_obj.to_html()
    ans2 = new_obj2.to_html()
    
    print(ans, ans2)

main()
