#!/usr/bin/env python3

# Find terms in CoNLL-U parses.

# The current implementation is intended as a simple example rather
# than a serious term recognition method.

import sys
import fileinput

import conllu

from collections import Counter


def argparser():
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument('file', nargs='+', metavar='CONLLU')
    return ap


def get_terms(conllu_data):
    """Get candidate terms from parsed text.
    
    Args:
        conllu_data (str): Parses in CoNLL-U format

    Returns:
        Dict of { term: weight } where term is normalized term text and
        weight an estimate of term relevance to data.
    """
    sentences = conllu.parse(conllu_data)

    # Naive example implementation: take lemma counts for nouns and return
    # counts normalized to [0,1] by dividing by max count.
    count = Counter()
    for sentence in sentences:
        for token in sentence:
            if token['upostag'] in ('NOUN', 'PROPN'):
                count[token['lemma']] += 1
    max_count = max(count.values())
    return { k: v/max_count for k, v in count.items() }


def main(argv):
    args = argparser().parse_args(argv[1:])
    for fn in args.file:
        with open(fn) as f:
            data = f.read()
        terms = get_terms(data)
        for t, v in sorted(terms.items(), key=lambda k: -k[1]):
            print('{:.2f}\t{}'.format(v, t))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
