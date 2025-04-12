from markdown_ import *

from blocktype import *

import os

from pathlib import Path


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_list = os.listdir(dir_path_content)
    for i in dir_list:
        direc = os.path.join(dir_path_content, i)
        dest_file_path = os.path.join(dest_dir_path, i)
        if os.path.isfile(direc):
            dest_file_path = Path(dest_file_path).with_suffix(".html")
            generate_page(direc, template_path, dest_file_path, basepath)
        else:
            generate_pages_recursive(direc, template_path, dest_file_path, basepath)

    




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



def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f_p = open(from_path, "r")
    f_p_content = f_p.read()
    f_p.close()

    t_p = open(template_path, "r")
    t_p_content = t_p.read()
    t_p.close()
    
    md_to_html_node = markdown_to_html_node(f_p_content)
    md_to_html = md_to_html_node.to_html()
    title = extract_title(f_p_content)

#code to extract title and content
    t_p_list = t_p_content.split("\n")
    new_t_p_list = []
    for i in t_p_list:
        if i.find("{{ Title }}") != -1:
            line = i.replace("{{ Title }}", title)
            f_line = line.replace('href="/', f'href="{basepath}/')
            new_t_p_list.append(f_line)
        elif i.find("{{ Content }}") != -1:
            line = i.replace("{{ Content }}", md_to_html)
            f_line = line.replace('href="/', f'href="{basepath}')
            new_t_p_list.append(f_line)
        else: new_t_p_list.append(i.replace('href="/', f'href="{basepath}'))
#---------
    t_p_content_actual = "\n".join(new_t_p_list)
    
    dir_pt = os.path.dirname(dest_path)   #this removes the file attached to the path provided


    if not os.path.exists(dir_pt):
        os.makedirs(dir_pt)
    d_p = open(dest_path, "w")
    d_p.write(t_p_content_actual)
    
    return "done"

