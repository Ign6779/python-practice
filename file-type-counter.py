# counts the types of files (by extension; .txt, .log, .conf) are in input directory

#!/usr/bin/env python3

import os

def file_type_counter(target_directory):
    extensions_dict = {}
    for file in os.walk(target_directory):
        root, ext = os.path.splitext(file)
        if ext in extensions_dict:
            extensions_dict[ext] += 1
        else:
            extensions_dict[ext] = 1

    for key, value in extensions_dict:
        print(f"{key}: {value}")


target_directory = input("Please input target directory")
file_type_counter(target_directory)
        

---------------------------------------------------------------------------------------
#fixed code

#!/usr/bin/env python3

import os

def file_type_counter(target_directory):
    extensions_dict = {}

    for dirpath, dirnames, filenames in os.walk(target_directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext:
                extensions_dict[ext] = extensions_dict.get(ext, 0) + 1

    for ext, count in extensions_dict.items():
        print(f"{ext}: {count}")

if __name__ == "__main__":
    target_directory = input("Please input target directory: ").strip()
    file_type_counter(target_directory)
