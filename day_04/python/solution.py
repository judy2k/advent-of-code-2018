#!/usr/bin/env python3

from collections import Counter
from itertools import accumulate
import re
from operator import itemgetter


def parse_line(line):
    match = re.search(r":(?P<min>\d+)(?:.*#(?P<guard_id>\d+))?", line)
    minute = int(match.group("min"))
    guard_id = match.group("guard_id")
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
        else:
            guards.setdefault(current_guard, []).append(ts)
    return ((guard_id, pairs(timestamps)) for guard_id, timestamps in guards.items())


def calculate(intervals):
    counter = Counter()
    time_asleep = 0
    for sleep, wake in intervals:
        counter.update({sleep: 1, wake: -1})
        time_asleep += wake - sleep
    event_times = sorted(counter.keys())
    sleep_counts = accumulate(counter.get(minute) for minute in event_times)
    return (*max(zip(event_times, sleep_counts), key=itemgetter(1)), time_asleep)


def load_intervals(path):
    lines = sorted(open(path, "r", encoding="utf-8").readlines())
    return [
        (guard_id, *calculate(intervals))
        for guard_id, intervals in guard_sleep_intervals(lines)
    ]


def solve(all_sleep_intervals):
    guard_id, minute, times, _ = max(all_sleep_intervals, key=itemgetter(-1))
    return guard_id * minute


def solve2(all_sleep_intervals):
    guard_id, minute, times, _ = max(all_sleep_intervals, key=itemgetter(-2))
    return guard_id * minute


def main():
    all_sleep_intervals = load_intervals("../input.txt")
    print(solve(all_sleep_intervals))
    print(solve2(all_sleep_intervals))


if __name__ == "__main__":
    main()
