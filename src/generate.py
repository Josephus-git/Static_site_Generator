from markdown_ import *

from blocktype import *

import os


def extract_title(markdown):
    md_list = markdown.split("\n")
    no_h1 = 0
    for i in md_list:
        if i[:2] == "# ":
            no_h1 += 1
            line = i
    if line == 0:
        raise Exception("no h1 heading")
    f_line = line.strip("#").strip(" ")
    return f_line



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f_p = open(from_path, "r")
    f_p_content = f_p.read()
    t_p = open(template_path, "r")
    t_p_content = t_p.read()
    md_to_html_node = markdown_to_html_node(f_p_content)
    md_to_html = md_to_html_node.to_html()
    title = extract_title(f_p_content)

#code to extract title and content
    t_p_list = t_p_content.split("\n")
    new_t_p_list = []
    for i in t_p_list:
        if i.find("{{ Title }}") != -1:
            line = i.replace("{{ Title }}", title)
            new_t_p_list.append(line)
        elif i.find("{{ Content }}") != -1:
            line = i.replace("{{ Content }}", md_to_html)
            new_t_p_list.append(line)
        else: new_t_p_list.append(i)
#---------
    t_p_content_actual = "\n".join(new_t_p_list)
    dir_pt = os.path.dirname(dest_path)
    if not os.path.exists:
        os.makedirs(dir_pt)
    
    d_p = open(dest_path, "w")
    d_p.write(t_p_content_actual)

    f_p.close()
    t_p.close()
    return "done"
    
