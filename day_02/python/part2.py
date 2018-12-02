#!/usr/bin/env python3

from itertools import combinations


def compare(id1, id2):
    differences = 0
    for l1, l2 in zip(id1, id2):
        if l1 != l2:
            differences += 1
        if differences > 1:
            return False
    return differences == 1


def common_letters(id1, id2):
    return ''.join(c1 for c1, c2 in zip(id1, id2) if c1 == c2)


def solve(ids):
    id_pairs = combinations(ids, 2)
    for id_pair in id_pairs:
        if compare(*id_pair):
            return common_letters(*id_pair)


def test_solve():
    assert solve([line.strip() for line in open('../sample_input2.txt')])


def test_common_letters():
    assert common_letters("fghij", "fguij") == 'fgij'


def test_compare():
    assert compare('abcde', 'abcde') is False
    assert compare('abcde', 'axcye') is False
    assert compare('fghij', 'fguij') is True


if __name__ == '__main__':
    print(solve(line.strip() for line in open('../input.txt')))
