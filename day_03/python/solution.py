#!/usr/bin/env python3

from collections import namedtuple
import re

import numpy as np


Claim = namedtuple("Claim", "id x y w h")


def load_claims(path):
    return [Claim(*(int(v) for v in re.findall(r"\d+", line))) for line in open(path, "r", encoding="utf-8")]


def main():
    cloth = np.zeros((1000, 1000), dtype=int)
    claims = load_claims("../input.txt")
    for c in claims:
        cloth[c.x : c.x + c.w, c.y : c.y + c.h] += 1
    print((cloth > 1).sum())

    for c in claims:
        if not (cloth[c.x: c.x + c.w, c.y: c.y + c.h] > 1).any():
            print(c.id)


if __name__ == "__main__":
    main()
