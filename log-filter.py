# takes lines from a logfile (format: 2024-03-15 13:22:41 [ERROR] Something bad happened), filters the last 7 days, and writes them onto a file named last_7_days.log

#!/usr/bin/env python3

import datetime

def log_filter(target_file):
    cuttoff_date = datetime.now() - datetime.timedelta(days=7)
    date_format = '%Y-%m-%d %H:%M:%S'

    try:
        with open(target_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{target_file}' not found.")
        return

    selected_lines = []

    for line in lines:
        line_date_string = line.split()[:2]
        line_date = datetime.strptime(line_date_string, date_format)

        if line_date < cuttoff_date:
            selected_lines.append(line)

    with open('last_7_days.log', 'w') as logf:
        logf.writelines(selected_lines)

log_filter(target_log_file)

---------------------------------------------------------------------------------------
#fixed code

#!/usr/bin/env python3

import datetime

def log_filter(target_file):
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=7)
    date_format = '%Y-%m-%d %H:%M:%S'

    try:
        with open(target_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{target_file}' not found.")
        return

    selected_lines = []

    for line in lines:
        try:
            timestamp_str = ' '.join(line.split()[:2])  # e.g., '2024-07-08 14:22:33'
            line_date = datetime.datetime.strptime(timestamp_str, date_format)

            if line_date >= cutoff_date:
                selected_lines.append(line)
        except Exception as e:
            print(f"Skipping malformed line: {line.strip()}")

    with open('last_7_days.log', 'w') as logf:
        logf.writelines(selected_lines)

    print(f"{len(selected_lines)} recent lines written to 'last_7_days.log'.")

if __name__ == "__main__":
    target_file = input("Enter path to log file: ").strip()
    log_filter(target_file)
