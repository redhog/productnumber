#! /usr/bin/python

import sys
import contextlib
import csv

if __name__ == '__main__':
    rows = csv.reader(sys.stdin, dialect='excel')
    headers = rows.next()
    out = csv.writer(sys.stdout, dialect='excel')
    out.writerow(headers)
    for row in rows:
        data = dict(zip(headers, row))
        if len(data['isbn']) == 10:
            data['isbn'] = '978' + data['isbn'][:-1]
            data['isbn'] += str((10 - sum((1 + 2 * (p % 2)) * int(d) for (p, d) in enumerate(data['isbn'])) % 10) % 10)
        out.writerow([data[key].encode('utf-8') for key in headers])
