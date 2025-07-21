#files have format: projectname-ddmmyyyy.txt
#find all files with that format. rename all files above a cuttofdate by adding -delete at the end

#!/usr/bin/env python3
import os
import re
import datetime

def file_rename_by_date(folder_path, cuttoff_date):
    cuttoff_date = datetime.strptime(cuttoff_date, %d%m%Y)

    for file in os.listdir(folder_path):
        res = re.findall("-(\d{8})", file)
        if not res: continue
        file_date = datetime.strptime(res[0], %d%m%Y)
        if file_date > cuttoff_date:
            os.rename(file, (res + "-delete.txt"))

folder_path = input("Input folder path: ")
cuttoff_date = input("Input cuttoff date (ddmmyyyy): ")

file_rename_by_date(folder_path, cuttoff_date)

---------------------------------------------------------------------------------------
#fixed code

#!/usr/bin/env python3

import os
import re
from datetime import datetime

def file_rename_by_date(folder_path, cutoff_date_str):
    # Convert input date string to datetime object
    try:
        cutoff_date = datetime.strptime(cutoff_date_str, "%d%m%Y")
    except ValueError:
        print("Invalid date format. Use ddmmyyyy.")
        return

    for filename in os.listdir(folder_path):
        # Match pattern like projectX-10032023.txt
        match = re.search(r"-(\d{8})", filename)
        if not match:
            continue  # Skip files without valid date

        try:
            file_date = datetime.strptime(match.group(1), "%d%m%Y")
        except ValueError:
            continue  # Skip malformed dates

        if file_date < cutoff_date:
            # Rename to add "-delete" before the file extension
            name_part, ext = os.path.splitext(filename)
            new_name = name_part + "-delete" + ext
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip()
    cutoff_date = input("Enter cutoff date (ddmmyyyy): ").strip()
    file_rename_by_date(folder_path, cutoff_date)
