# change a 'server_ip' line in a config file with a new IP. Add the line if it does not exist

#!/usr/bin/env python3

import re

def ip_replacer(config_file, ip_address):
    try:
        with open(config_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{config_file}' not found.")
        return

    new_lines = []
    pattern = re.compile(rf'^("server_ip"\s*=)(.*)$')
    found = False

    for line in lines:
        stripped_line = line.rstrip('\n')

        match = pattern.match(stripped_line)
        if match:
            found = True
            config, ip = match.groups()
            new_line = config + ip_address
        else:
            new_lines.append(line)

        if not found:
            new_lines.append(f"server_ip={ip_address}")

    with open(config_file, 'w') as f:
        f.writelines(new_lines)

    print(f"Changed ip address to {ip_address}")

config_file = input("Input config file to change: ")
ip_address = input("Input desired IP address: ")

ip_replacer(config_file, ip_address)

---------------------------------------------------------------------------------------
#fixed code

#!/usr/bin/env python3

import re

def ip_replacer(config_file, ip_address):
    try:
        with open(config_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{config_file}' not found.")
        return

    new_lines = []
    pattern = re.compile(r'^server_ip\s*=\s*.*$')
    found = False

    for line in lines:
        if pattern.match(line.strip()):
            new_lines.append(f"server_ip={ip_address}\n")
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"server_ip={ip_address}\n")

    with open(config_file, 'w') as f:
        f.writelines(new_lines)

    print(f"Set server_ip to {ip_address}.")

if __name__ == "__main__":
    config_file = input("Input config file to change: ").strip()
    ip_address = input("Input desired IP address: ").strip()
    ip_replacer(config_file, ip_address)
