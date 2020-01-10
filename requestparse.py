#!/usr/bin/env python3

# Request CoNLL-U analyses from remote service.

import sys
import fileinput

import requests


# Turku Neural Parser demo URL. For anything more than small-scale
# experiments, please run your own parser server; instructions:
# https://turkunlp.org/Turku-neural-parser-pipeline/docker.html

DEFAULT_URL ='http://bionlp-www.utu.fi/parser_demo/parsefile'
# DEFAULT_URL = 'http://bionlp-www.utu.fi/parser_demo/'

# Default model to use for requested parses.
DEFAULT_MODEL = 'Finnish-neural'


def request_parse(text, model=DEFAULT_MODEL, url=DEFAULT_URL):
    data = {
        'data_file': text,
    }
    r = requests.post(url, files=data)
    return r.text

                  
def main(argv):
    for line in fileinput.input():
        line = line.rstrip('\n')
        if line:
            print(request_parse(line))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
