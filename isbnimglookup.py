#!/usr/bin/python
import sys
import zbar
import Image
import os
import os.path
import csv

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
scanner.parse_config('isbn10.disable')

out = csv.writer(sys.stdout, dialect='excel')
out.writerow(['img', 'isbn'])

for dirpath, dirnames, filenames in os.walk("."):
    filenames.sort()
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        try:
            pil = Image.open(filepath).convert('L')
        except Exception, e:
            sys.stderr.write("%s: %s\n" % (filepath, e))
            continue
        width, height = pil.size
        image = zbar.Image(width, height, 'Y800', pil.tostring())
        scanner.scan(image)
        symbols = [symbol for symbol in image]
        if symbols:
            # symbols[0].type
            out.writerow([filepath, symbols[0].data])
        else:
            out.writerow([filepath, ''])
        del(image)
