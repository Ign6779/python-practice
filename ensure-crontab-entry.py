# ensure that the crontab for the current user has a specific job line (doesn't mention if input or not). If it's there, do nothing. If it's missing, add it
# e.g. input: 0 2 * * * /usr/local/bin/backup.sh

#!/usr/bin/env python3

import subprocess

def run_backup():
    cronjobs = subprocess.run(["crontab", "-l"])
    exists = False
    for job in cronjobs:
        if str(job) == "0 2 * * * /usr/local/bin/backup.sh"
            print("crontab job already exist", job)
            exists = True
            break

    if not exists:
        subprocess.run(["crontab", ])
  

---------------------------------------------------------------------------------------
# fixed code

#!/usr/bin/env python3

import subprocess

def ensure_cron_job(target_line):
    # Get current crontab (if any)
    try:
        result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, check=True)
        current_cron = result.stdout.splitlines()
    except subprocess.CalledProcessError:
        # No crontab set for user (treated as empty)
        current_cron = []

    if target_line in current_cron:
        print("Cron job already exists.")
        return

    print("Cron job not found. Adding it.")
    new_cron = '\n'.join(current_cron + [target_line]) + '\n'

    # Pipe the new cron back into crontab
    subprocess.run(["crontab", "-"], input=new_cron, text=True)
    print("Cron job added.")

if __name__ == "__main__":
    cron_line = "0 2 * * * /usr/local/bin/backup.sh"
    ensure_cron_job(cron_line)
