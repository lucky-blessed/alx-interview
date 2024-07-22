#!/usr/bin/python3
"""
Log parsing script
"""


import sys

def print_stats(total_size, status_counts):
    """
    Print matrics accumulation
    """
    print("File size: {}".format(total_size))
    for ststus in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) > 6:
                size = int(parts[-1])
                status = int(parts[-2])
                total_size += size
                if status in status_counts:
                    status_counts[status] += 1
        except (ValueError, IndexError):
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

print_stats(total_size, status_counts)


