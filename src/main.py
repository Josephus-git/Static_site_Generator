from textnode import *
from htmlnode import *
from update_public import *
from generate import *

def main():
    
    copy_to_public()
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    print(generate_page(from_path, template_path, dest_path))

main()
