#!/usr/bin/env python3

from collections import Counter
from itertools import groupby, accumulate
import re
from operator import itemgetter


def parse_line(line):
    match = re.match(r'\[\d+-\d+-\d+ \d+:(?P<min>\d+)\](?:.*#(?P<guard_id>\d+))?', line)
    minute = int(match.group('min'))
    guard_id = match.group('guard_id')
    return minute, int(guard_id) if guard_id else None


def pairs(seq):
    return list(zip(*[iter(seq)] * 2))


def guard_sleep_intervals(lines):
    guards = {}
    current_guard = None
    for line in lines:
        ts, guard_id = parse_line(line)
        if guard_id is not None:
            current_guard = guard_id
            guards.setdefault(guard_id, [])
        else:
            guards[current_guard].append(ts)
    return {guard_id: pairs(timestamps) for guard_id, timestamps in guards.items()}


def sleep_seconds(ts_pairs):
    return sum((e-s) for s, e in ts_pairs)


def sleepiest_guard(sleep_intervals):
    total_sleeps = Counter({guard_id: sleep_seconds(intervals) for guard_id, intervals in sleep_intervals.items()})
    guard_id, _ = total_sleeps.most_common(1)[0]
    return guard_id


def sleepiest_minute(intervals):
    if not intervals:
        return 0, 0
    sleeping, waking = [Counter(ts) for ts in zip(*intervals)]
    pairs = enumerate(accumulate((sleeping.get(minute, 0) - waking.get(minute, 0)) for minute in range(60)))
    minute, count = max(pairs, key=itemgetter(1))
    return minute, count


def load_intervals(path):
    lines = sorted(open(path, 'r', encoding='utf-8').readlines())
    return guard_sleep_intervals(lines)


def solve(all_sleep_intervals):
    sleepy = sleepiest_guard(all_sleep_intervals)
    minute, times = sleepiest_minute(all_sleep_intervals[sleepy])
    return sleepy * minute


def solve2(all_sleep_intervals):
    guard_records = ((guard_id, *sleepiest_minute(intervals)) for guard_id, intervals in all_sleep_intervals.items())
    guard_id, minute, times = max(guard_records, key=itemgetter(-1))
    return guard_id * minute


def main():
    all_sleep_intervals = load_intervals("../input.txt")
    print(solve(all_sleep_intervals))
    print(solve2(all_sleep_intervals))


def test_parse_line():
    assert parse_line("[1518-04-10 23:52] Guard #3559 begins shift") == (52, 3559)
    assert parse_line("[1518-04-10 23:52] wakes up") == (52, None)


def test_solve():
    assert solve(load_intervals("../sample_input.txt")) == 240
    assert solve(load_intervals("../input.txt")) == 87681


def test_solve2():
    assert solve2(load_intervals("../sample_input.txt")) == 4455
    assert solve2(load_intervals("../input.txt")) == 136461


if __name__ == '__main__':
    main()
