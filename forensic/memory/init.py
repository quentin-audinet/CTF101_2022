import os
import random as rd

PATH = "./disk"

def create_dir(n, current_path):
    if n == 0:
        return
    else:
        for i in range(8):
            new_dir = hex(rd.randint(0x10000, 0x100000))[2:]
            while(os.path.exists(current_path + "/" + new_dir)):
                new_dir = hex(rd.randint(0x1000, 0x10000))[2:]
            os.mkdir(current_path + "/" + new_dir)
            create_dir(n-1, current_path + "/" + new_dir)

create_dir(6, PATH)
