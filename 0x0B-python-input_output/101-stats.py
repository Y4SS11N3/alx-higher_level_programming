#!/usr/bin/python3
"""Log parsing script to compute metrics from stdin input."""

import sys

status_codes = {
    str(code): 0 for code in [
        200, 301, 400, 401, 403, 404, 405, 500
    ]
}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 1:
            status = parts[-2]
            size = parts[-1]

            if status in status_codes:
                status_codes[status] += 1
            try:
                total_size += int(size)
            except ValueError:
                pass

        line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
