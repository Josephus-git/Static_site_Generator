import os

import shutil


def copy_to_public():
    def copy_actual(path_dir, current_public_path):
        new_dir_lst = os.listdir(path=path_dir)
        for i in new_dir_lst:
            path_ = os.path.join(path_dir, i)
            if os.path.isfile(path_):
                shutil.copy(path_, current_public_path)
                log.append(f"copied {path_} to {current_public_path}")
            else: 
                new_path_in_public = os.path.join(current_public_path, i)
                os.mkdir(new_path_in_public)
                copy_actual(path_, new_path_in_public) 
        return log

    if os.path.exists("public"):
        shutil.rmtree("public")
        os.mkdir("public")
    else: os.mkdir("public")

    log = []
    
    return copy_actual("static", "public")

