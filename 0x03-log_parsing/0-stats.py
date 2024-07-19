#!/usr/bin/python3
import sys
import re
import signal

# Regular expression to match the log line format
log_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

# Status codes we are interested in
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Variables to hold metrics
total_file_size = 0
status_code_count = {code: 0 for code in valid_status_codes}

# Function to handle keyboard interrupt (CTRL + C)
def keyboard_interrupt_handler(signal, frame):
    print_stats()
    sys.exit(0)

# Registering signal handler for interrupt
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

# Function to print current stats
def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

# Main loop to read stdin
try:
    for line in sys.stdin:
        line = line.strip()
        # Match log line format
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            if status_code in valid_status_codes:
                total_file_size += file_size
                status_code_count[status_code] += 1
        # Print stats after every 10 lines
        if len(status_code_count) > 0 and sum(status_code_count.values()) % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    keyboard_interrupt_handler(signal.SIGINT, None)

