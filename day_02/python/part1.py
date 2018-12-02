#!/usr/bin/env python3

from collections import Counter
from operator import mul


def components(s):
    counts = {*Counter(s).values()}
    return (2 in counts), (3 in counts)


def component_counts(components):
    return tuple(sum(col) for col in zip(*components))


def solve(path):
    return mul(*component_counts(components(line.strip()) for line in open(path, 'r', encoding='utf-8')))


def test_components():
    assert components("abcdef") == (False, False)
    assert components("bababc") == (True, True)
    assert components("abbcde") == (True, False)
    assert components("abcccd") == (False, True)
    assert components("aabcdd") == (True, False)
    assert components("abcdee") == (True, False)
    assert components("ababab") == (False, True)


def test_counts():
    assert component_counts(
        [
            (False, False),
            (True, True),
            (True, False),
            (False, True),
            (True, False),
            (True, False),
            (False, True),
        ]
    ) == (4, 3)


def test_sample():
    assert solve('../sample_input.txt') == 12


if __name__ == '__main__':
    print(solve('../input.txt'))
