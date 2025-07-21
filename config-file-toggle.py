#!/usr/bin/env python3

#takes file path and line as arguments. if line exists, it is removed. if it does not exist, it is added.

import os

filepath = input("Enter filepath: ")
searchLine = input("Enter line: ")

with open('filepath', 'r') as f:
  lines = f.readlines()

with open('filepath', 'w') as f:
  foundLine = false
  for line in lines:
    if line.strip('\n') != searchLine
      f.write(line)
    else:
      foundLine = true
  if !foundLine:
    f.write(searchLine)


--------------------------------------------------------------------------------------
#fixed code

#!/usr/bin/env python3

filepath = input("Enter filepath: ")
searchLine = input("Enter line: ")

try:
    with open(filepath, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

foundLine = False
with open(filepath, 'w') as f:
    for line in lines:
        if line.strip('\n') != searchLine:
            f.write(line)
        else:
            foundLine = True
    if not foundLine:
        f.write(searchLine + '\n')

---------------------------------------------------------------------------------------
#ideal code

#!/usr/bin/env python3

import sys
import os

def toggle_line(filepath, target_line):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Normalize both the target and file lines (remove trailing newline)
    lines_stripped = [line.rstrip('\n') for line in lines]

    # Decide action
    if target_line in lines_stripped:
        # Remove all matching lines
        new_lines = [line for line in lines_stripped if line != target_line]
        print(f"Removed line: '{target_line}'")
    else:
        new_lines = lines_stripped + [target_line]
        print(f"Added line: '{target_line}'")

    # Write back to file
    with open(filepath, 'w') as file:
        file.writelines(line + '\n' for line in new_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./toggle_line.py <file> <line>")
        sys.exit(1)

    filepath = sys.argv[1]
    target_line = sys.argv[2]

    toggle_line(filepath, target_line)