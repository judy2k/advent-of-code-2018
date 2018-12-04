from solution import *


def test_parse_line():
    assert parse_line("[1518-04-10 23:52] Guard #3559 begins shift") == (52, 3559)
    assert parse_line("[1518-04-10 23:52] wakes up") == (52, None)


def test_solve():
    assert solve(load_intervals("../sample_input.txt")) == 240
    assert solve(load_intervals("../input.txt")) == 87681


def test_solve2():
    assert solve2(load_intervals("../sample_input.txt")) == 4455
    assert solve2(load_intervals("../input.txt")) == 136461
