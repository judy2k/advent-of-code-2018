#!/usr/bin/env python3

from itertools import accumulate, chain, cycle


def changes(path):
    return cycle(int(line) for line in open(path, encoding="utf-8"))


def frequencies(change_iter):
    return accumulate(chain([0], change_iter))


def first_seen_frequency(path):
    seen_frequencies = set()
    for frequency in frequencies(changes(path)):
        if frequency in seen_frequencies:
            return frequency
        seen_frequencies.add(frequency)


print(first_seen_frequency("input.txt"))
