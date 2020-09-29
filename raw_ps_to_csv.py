#!/usr/bin/env python

import sys
import os
import re

# cd to file dir
pwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(pwd)
logs = sys.argv[1:]
runs = -1
resdict = dict()


def formatline(path, line):
    global runs, resdict

    if re.search(r'^%', line):
        return

    match = re.search(r'(?P<cpu>\d{1,3}(\.\d)?)\s+(?P<mem>\d+)\s+(?P<process>[a-z/_\.\-\d]+)\s+?(--type=(?P<chrome_type>[a-z-]+))?', line)
    if match:
        cpu = int(float(match.group('cpu')))
        mem = int(match.group('mem'))
        process = match.group('process').rstrip().split('/')[-1]
        chrometype = match.group('chrome_type')
        
        key = process
        if (chrometype is not None):
            key = f'{key} {chrometype}'
        for _key,val in {'cpu':cpu, 'mem':mem}.items():
            akey = f'{key} {_key}'
            try: resdict[akey].append(val)
            except:
                tmp = []
                if len(resdict.keys()) >= 1:
                    tmp = [0 for x in resdict[list(resdict.keys())[0]]]
                tmp.append(val)
                resdict[akey] = tmp
        return

    match = re.search(r'(?P<sec>\d+)\.(?P<ms>\d+)elapsed', line)
    if match:
        total = int(match.group('sec')) * 1000 \
              + int(match.group('ms'))  * 10

        runs += 1
        ext = os.path.split(path)[1].split('-')[-1].split('.')[0]
        _dir = 'formatted'
        if ext != 'result': _dir +=  f'_{ext}'
        _dir = os.path.join(os.path.split(path)[0], _dir)
        os.makedirs(_dir, exist_ok=True)
        with open(os.path.join(_dir, f'{runs}.csv'), 'w') as _file:
            _file.write(','.join([str(x) for x in resdict.keys()]) + '\n') # header
            stop = [len(x) for x in resdict.values()]
            stop.sort(reverse=True)

            for i in range(0, stop[0]):
                k = ''
                for j in resdict.keys():
                    try: val = str(resdict[j][i])
                    except: val = '0'
                    k += f'{val},'
                _file.write(k[:-1] + '\n')
        resdict = dict() # reset result to write


for f in logs:
    resdict = dict()
    with open(f, 'r') as log:
        for line in log:
            formatline(f, line)
