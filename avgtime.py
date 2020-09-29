#!/usr/bin/env python

import sys
import os
import re
import numpy as np

# cd to file dir
pwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(pwd)
logs = sys.argv[1:]
total = list()

def formatline(line):
    global total
    match = re.search(r'(?P<sec>\d+)\.(?P<ms>\d+)elapsed', line)
    if match:
        _total = int(match.group('sec')) * 1000 \
              + int(match.group('ms'))  * 10

        total.append(_total)


for f in logs:
    total = list()
    with open(f, 'r') as log:
        for line in log:
            formatline(line)

    print(np.average(np.array(total)))
