#!/usr/bin/env python3

with open("../input.txt", encoding="utf-8") as fin:
    print(sum(int(line) for line in fin))
