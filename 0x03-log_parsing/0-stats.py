#!/usr/bin/python3
"""
Log Parsing Script

This script reads log entries from stdin, parses them according to a specific format,
and computes metrics including total file size and counts of specific HTTP status codes.
It handles keyboard interrupts (Ctrl+C) gracefully by printing current metrics before exiting.

Input format expected:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Metrics computed and displayed after every 10 lines processed:
- Total file size accumulated.
- Count of lines by HTTP status code: 200, 301, 400, 401, 403, 404, 405, 500

Requirements:
- Python 3.4.3 or higher.
- PEP 8 style compliance.
- Graceful handling of keyboard interrupts.
"""

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
    """Handler for keyboard interrupt (Ctrl+C). Prints current stats and exits."""
    print_stats()
    sys.exit(0)

# Registering signal handler for interrupt
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

# Function to print current stats
def print_stats():
    """Prints the current accumulated metrics."""
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
