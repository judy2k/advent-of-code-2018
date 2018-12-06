#!/usr/bin/env python3

from collections import Counter
from itertools import product
from operator import itemgetter


def read_file(path):
    return [tuple(int(c) for c in line.split(', ')) for line in open(path, 'r', encoding='utf-8')]


def in_region(x, y, coordinates, threshold):
    tally = 0
    for c in coordinates:
        tally += abs(x - c[0]) + abs(y - c[1])
        if tally >= threshold:
            return 0
    return 1


def main():
    coordinates = read_file('../input.txt')
    min_x, min_y = (min(v) for v in zip(*coordinates))
    max_x, max_y = (max(v) for v in zip(*coordinates))

    counts = Counter()
    for x, y in product(range(min_x, max_x+1), range(min_y, max_y+1)):
        nearest_points = sorted([(point, abs(x - point[0]) + abs(y - point[1])) for point in coordinates], key=itemgetter(1))
        if nearest_points[0][1] != nearest_points[1][1]:
            counts[nearest_points[0][0]] += 1
    print(counts.most_common(1)[0][1])

    print(sum(in_region(x, y, coordinates, 10_000) for x, y in product(range(min_x, max_x+1), range(min_y, max_y+1))))


def test_in_region():
    cs = read_file('../sample_input.txt')
    assert in_region(4, 3, cs, 32) == True
    assert in_region(4, 2, cs, 32) == False


if __name__ == '__main__':
    main()
