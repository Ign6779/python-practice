# removes files older than input age from input folder

#!/usr/bin/env python3

import os
import datetime

def remove_files_by_age(target_directory, cuttoff_age):
    current_day = date.today()
    for file in os.listdir(target_directory):
        file_path = os.path.join(target_directory, file)
        file_creation_date = os.path.getmtime(file_path)
        file_age = current_day - file_creation_date
        if file_age > cuttoff_age:
            os.remove(file_path)

target_directory = input("Target directory: ")
cuttoff_age = input("Cuttoff date: ")

remove_files_by_age(target_directory, cuttoff_age)

---------------------------------------------------------------------------------------
#fixed code

#!/usr/bin/env python3

import os
import datetime

def remove_files_by_age(target_directory, max_age_days):
    current_day = datetime.datetime.now()

    for file in os.listdir(target_directory):
        file_path = os.path.join(target_directory, file)

        if not os.path.isfile(file_path):
            continue  # skip subdirectories

        # Get last modification time
        mtime = os.path.getmtime(file_path)
        file_mod_time = datetime.datetime.fromtimestamp(mtime)
        file_age = (current_day - file_mod_time).days

        if file_age > max_age_days:
            try:
                os.remove(file_path)
                print(f"Deleted: {file} (Age: {file_age} days)")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")

if __name__ == "__main__":
    target_directory = input("Target directory: ").strip()
    try:
        max_age_days = int(input("Delete files older than how many days? ").strip())
    except ValueError:
        print("Invalid number of days.")
        exit(1)

    remove_files_by_age(target_directory, max_age_days)
