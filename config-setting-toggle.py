# toggles setting_name on/off (commented/uncommented) on target file

#!/user/bin/env python3

def toggle_setting(target_file, setting_name):
    # getting the lines in the file
    try:
        with open(target_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    lines_stripped = [line.rstrip('\n') for line in lines]

    #matching lines to setting_name
    new_lines = []
    for line in lines_stripped:
        match = re.search(setting_name, line)
        if not match:
            continue
        if re.match(r"#"+setting_name, line)
            line = setting_name
        else:
            line = "#"+setting_name

        new_lines.append(line)

    with open(target_file, 'w') as f:
        f.writelines(line + '\n' for line in new_lines)

target_file = input("Target config file: ")
setting_name = input("Target setting to toggle: ")

toggle_setting(target_file, setting_name)


---------------------------------------------------------------------------------------
# fixed code

#!/usr/bin/env python3

import re

def toggle_setting(target_file, setting_name):
    try:
        with open(target_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{target_file}' not found.")
        return

    new_lines = []

    # Pattern to match: line with optional # followed by setting_name and an equal sign
    pattern = re.compile(rf'^(\s*#?\s*)({re.escape(setting_name)}\s*=.*)$')

    for line in lines:
        stripped_line = line.rstrip('\n')

        match = pattern.match(stripped_line)
        if match:
            # If it's commented, uncomment it
            prefix, rest = match.groups()
            if prefix.strip().startswith('#'):
                new_line = rest
            else:
                new_line = '#' + rest
            new_lines.append(new_line + '\n')
        else:
            # Keep line unchanged
            new_lines.append(line)

    with open(target_file, 'w') as f:
        f.writelines(new_lines)

    print(f"Toggled setting '{setting_name}' in '{target_file}'.")

if __name__ == "__main__":
    target_file = input("Target config file: ").strip()
    setting_name = input("Setting name to toggle: ").strip()
    toggle_setting(target_file, setting_name)
