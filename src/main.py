from update_public import *

import sys

from generate import *


def main():
    if sys.argv[1] is None:
        sys.argv[1] = "/"

    basepath = sys.argv[1]


    from_path = basepath + "content"
    static = basepath + "static"
    template_path = basepath + "template.html"
    dest_path = basepath + "public"

    copy_to_public(static, dest_path)
    print(generate_pages_recursive(from_path, template_path, dest_path))



main()
