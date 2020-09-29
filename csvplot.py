#!/usr/bin/env python

import sys
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('xtick', labelsize=30)
rc('ytick', labelsize=30)


# cd to file dir
pwd = os.path.dirname(os.path.realpath(__file__))
dirs = list()
savedir = Path.home()
for arg in sys.argv[1:]:
    if os.path.isabs(arg):
        dirs.append(arg)
        continue
    
    dirs.append(os.path.join(pwd, arg))


def filtercols(df, allowed=['node', 'chrom', 'firefox', 'php', 'phantomjs']):
    for x in df.columns:
        found = False
        for y in allowed:
            if y in x:
                found = True
                break
        if not found: df.drop(x, axis=1, inplace=True)

    return df

def avgcol(df, cols='all'):
    if cols != 'all': cols=[cols]
    else: cols=df.columns

    res = dict()
    for x in cols:
        arr = df[x].to_numpy()

        # remove preceeding zeros
        for i in range(0, len(arr)):
            if i > 0:
                break

        # remove trailing zeros
        stop = len(arr)-1
        for j in range(len(arr)-1, -1, -1):
            if j > 0:
                break

        res[x] = np.average(arr[i:j])

    return res


for _dir in dirs:
    plt.figure(figsize=(17,10), tight_layout=True)
    plt.suptitle('Resource usage', fontsize=30)
    axmem = plt.subplot(121)
    plt.xticks(rotation=33, horizontalalignment='right')
    axmem.set_ylabel('Average memory usage in KiB', fontsize=30)
    # axmem.set_ylim([0, 75000])
    axmem.set_ylim([0, 120000])
    axcpu = plt.subplot(122)
    plt.xticks(rotation=33, horizontalalignment='right')
    axcpu.set_ylabel('Average cpu usage in %', fontsize=30)
    # axcpu.set_ylim([0, 25])
    axcpu.set_ylim([0, 30])

    total = dict()
    base = os.path.split(os.path.split(_dir)[0])[1]
    ext = os.path.split(_dir)[1].split('_')[-1]
    filename = f'{base}.png'
    if ext != 'formatted': filename = f'{base}_{ext}.png'
    
    loc = os.path.join(savedir, filename)
    print(loc)

    with os.scandir(_dir) as files:
        for _file in files:
            csv = filtercols(pd.read_csv(_file.path))
            avgs = avgcol(csv)
            for key,val in avgs.items():
                try: total[key].append(val)
                except: total[key] = [val]

        for key,val in total.items():
            label = key.split(' ')[-2].split('-')[-1]
            if 'mem' in key:
                print(label, np.average(np.array(val)))
                axmem.bar(label, np.average(np.array(val)))
            elif 'cpu' in key:
                axcpu.bar(label, np.average(np.array(val)))

        plt.savefig(loc)
        # plt.show()
