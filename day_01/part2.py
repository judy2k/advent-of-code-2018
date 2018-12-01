#!/usr/bin/env python3

from itertools import accumulate, chain, cycle


def first_seen_frequency(path):
    seen_frequencies = set()
    for frequency in accumulate(
        chain([0], cycle(int(line) for line in open(path, encoding="utf-8")))
    ):
        if frequency in seen_frequencies:
            return frequency
        seen_frequencies.add(frequency)


print(first_seen_frequency("input.txt"))
