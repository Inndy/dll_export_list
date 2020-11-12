import glob
import json
import os
import sys

import lief

print('[+]', 'You are using lief version:', lief.__version__)

out_path = os.path.join(os.path.dirname(__file__), 'db.txt')
with open(out_path, 'a') as fp_out:
    for pattern in sys.argv[1:]:
        for path in glob.iglob(pattern):
            # erase from cursor to line end, reset cursor to line begin
            print('[*]', path, end='\x1b[0K\r', flush=True)
            basename = os.path.basename(path)

            pe = lief.parse(path)
            if not pe.has_exports:
                continue
            for f in pe.exported_functions:
                print('%s\t%s' % (basename, f), file=fp_out)
