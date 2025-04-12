from update_public import *

import sys

from generate import *


def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else: basepath = sys.argv[1]


    from_path = "./content"
    static = "./static"
    template_path = "./template.html"
    dest_path = "./docs"
    print(from_path)

    copy_to_public(static, dest_path)
    print(generate_pages_recursive(from_path, template_path, dest_path, basepath))



main()
