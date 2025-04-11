from update_public import *

from generate import *


def main():
    
    from_path = "content"
    static = "static"
    template_path = "template.html"
    dest_path = "public"

    copy_to_public(static, dest_path)
    print(generate_pages_recursive(from_path, template_path, dest_path))



main()
