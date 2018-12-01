#!/usr/bin/env python3

from itertools import accumulate, chain, cycle


def changes(path):
    return cycle(int(line) for line in open(path, encoding='utf-8'))


def frequencies(change_iter):
    return accumulate(chain([0], change_iter))


seen_frequencies = set()
for frequency in frequencies(changes('input.txt')):
    if frequency in seen_frequencies:
        print(frequency)
        break
    seen_frequencies.add(frequency)
