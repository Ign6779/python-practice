# remove files in directory ending in .tmp or .temp that are older than 1 day

#!/usr/bin/env python3

import os
import datetime

def temp_files_cleaner(target_directory):
    current_day = datetime.datetime.now()

    for file in os.listdir(target_directory):
        file_path = os.path.join(target_directory, file)

        if not os.path.isfile(file_path):
            continue

        if file.endswith(".tmp") or file.endswith(".temp"):
            mtime = os.path.getmtime(file_path)
            file_mod_time = datetime.datetime.fromtimestamp(mtime)
            file_age = (current_day - file_mod_time).days

            if file_age > 1:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file} (Age: {file_age} days)")
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")

if __name__ == "__main__":
    target_directory = input("Target directory: ").strip()
    temp_files_cleaner(target_directory)