# ensure a file secret.txt exists on input dir
# ensure secret.txt has owner root, group root & permissions rw-------
# exit code must be non-zero if it fails

#!/usr/env/bin python3

import os
import pwd
import grp

def enforce_file_status(input_dir):
    file_path = os.path.join(input_dir, "secret.txt")

    if os.path.isfile(file_path):
        #straight up just forcing the ownership and group
        os.chown(file_path, 0, 0)
        
        #and just directly setting file perms
        os.chmod(file_path, 600)
        
    else:
        print("File secret.txt not found in directory")
        exit



input_dir = input("Input dir: ")
enforce_file_status(input_dir)

---------------------------------------------------------------------------------------
# fixed code

#!/usr/bin/env python3

import os
import pwd
import grp
import stat
import sys

def enforce_file_status(input_dir):
    file_path = os.path.join(input_dir, "secret.txt")

    try:
        # Ensure file exists
        if not os.path.exists(file_path):
            print("File not found. Creating it.")
            with open(file_path, 'w') as f:
                f.write('')  # create empty file

        # Get UID and GID for 'root'
        uid = pwd.getpwnam("root").pw_uid
        gid = grp.getgrnam("root").gr_gid

        # Set ownership
        os.chown(file_path, uid, gid)

        # Set permissions to rw-------
        os.chmod(file_path, 0o600)

        print("File is now enforced correctly.")
        return 0  # success

    except Exception as e:
        print(f"Error: {e}")
        return 1  # failure

if __name__ == "__main__":
    input_dir = input("Input dir: ").strip()
    exit_code = enforce_file_status(input_dir)
    sys.exit(exit_code)
