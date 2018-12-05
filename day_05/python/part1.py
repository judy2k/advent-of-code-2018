#!/usr/bin/env python3


def process(s):
    done = []
    to_do = list(reversed(s))
    while to_do:
        a = to_do.pop()
        if to_do:
            b = to_do[-1]
            if a != b and a.lower() == b.lower():
                to_do.pop()
                if done:
                    to_do.append(done.pop())
            else:
                done.append(a)
        else:
            done.append(a)
    return len(done)


def part1():
    print(process(open('../input.txt', encoding='utf-8').read().strip()))


def part2():
    s = open('../input.txt', encoding='utf-8').read().strip()
    print(min(process([c for c in s if c.lower() != char]) for char in set(s.lower())))


if __name__ == '__main__':
    part1()
    part2()
