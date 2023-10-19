#!/usr/bin/env python3

"""
    Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size> (see input format above)
    Number of lines by status code:
    possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    format: <status code>: <number>
    status codes should be printed in ascending order
"""


import sys
import re
from collections import defaultdict

# Regular expression to match the input format
log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[([^]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

# Initialize variables
total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            line_count += 1
            ip, _, status_code, file_size = match.groups()
            total_size += int(file_size)
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[status_code] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print("Total file size:", total_size)
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")
                print()

except KeyboardInterrupt:
    # Handle CTRL+C to print the statistics and exit gracefully
    print("\nTotal file size:", total_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

# Final statistics if there are remaining lines
if line_count % 10 != 0:
    print("\nTotal file size:", total_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
