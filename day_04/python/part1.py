#!/usr/bin/env python3

from collections import Counter
from datetime import datetime
from itertools import groupby
import re


def parse_line(line):
    match = re.match(r'\[(?P<ts>.*)\](?:.*#(?P<guard_id>\d+))?', line)
    ts = datetime.strptime(match.group('ts'), '%Y-%m-%d %H:%M')
    guard_id = match.group('guard_id')
    return ts, int(guard_id) if guard_id else None


def guard_timestamps(guard_dates, timestamps):
    print(guard_dates)
    result = {}
    for day, group in groupby(timestamps, datetime.date):
        result.setdefault(guard_dates[day], []).extend(list(group))
    return result


def pairs(seq):
    return list(zip(*[iter(seq)] * 2))


def sleep_seconds(ts_pairs):
    return sum((e-s).seconds for s, e in ts_pairs) // 60


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


def sleepiest_guard(sleep_intervals):
    return Counter({guard_id: sleep_seconds(pairs) for guard_id, pairs in sleep_intervals.items()}).most_common(1)[0][0]


def solve(input_file):
    lines = sorted(open(input_file, 'r', encoding='utf-8').readlines())
    all_sleep_intervals = guard_sleep_intervals(lines)
    sleepy = sleepiest_guard(all_sleep_intervals)
    sleeping, waking = [Counter(t.minute for t in ts) for ts in zip(*all_sleep_intervals[sleepy])]
    counter = 0
    max_counter = 0
    max_minute = 0
    for minute in range(60):
        counter += sleeping.get(minute, 0)
        counter -= waking.get(minute, 0)
        if counter > max_counter:
            max_counter = counter
            max_minute = minute
    return sleepy * max_minute


def main():
    print(solve('../input.txt'))


def test_parse_line():
    assert parse_line("[1518-04-10 23:52] Guard #3559 begins shift") == (datetime(1518, 4, 10, 23, 52), 3559)
    assert parse_line("[1518-04-10 23:52] wakes up") == (datetime(1518, 4, 10, 23, 52), None)


def test_solve():
    assert solve("../sample_input.txt") == 240


if __name__ == '__main__':
    main()
