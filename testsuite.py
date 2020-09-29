#!/usr/bin/python

import sys
import os
import time
import yaml
ACCEPTANCE_TEST_DELAY=5
BROWSER_CONTAINER='selenium-server'

os.chdir(os.path.dirname(os.path.realpath(__file__)))

tests = []
needs_browser_container = ['accept-dusk', 'dusk', 'webdriverio']
with open('docker-compose.yml', 'r') as stream:
    tests = list(yaml.safe_load(stream)['services'].keys())

runs = sys.argv[-1]

if not runs.isnumeric():
    print('Last argument needs to be a numeric value (n. iterations)')
    exit(1)

runs = int(runs)

if sys.argv[1] != 'all':
    proposedTests = sys.argv[1:-1]

    for test in proposedTests:
        if not test in tests:
            print(f'{test} is not valid')
            exit(1)

    tests = proposedTests

os.system('sudo docker-compose down')

for test in tests:
    os.system(f'sudo docker-compose build {test}')
    if test in needs_browser_container:
        os.system(f'sudo docker-compose up -d {BROWSER_CONTAINER}')
    for i in range(0, runs):
        os.system(f'sudo docker-compose up -d {test}')
        os.system(f'sudo docker-compose stop {test}')
        os.system(f'sudo docker-compose rm -f {test}')

        if test.startswith('accept'):
            time.sleep(ACCEPTANCE_TEST_DELAY)
