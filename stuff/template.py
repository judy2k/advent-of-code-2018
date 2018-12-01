#!/usr/bin/env python3

import argparse
import logging
import sys


def parse_args(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    arguments = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if arguments.verbose else logging.WARNING)
    return arguments


def main(argv=sys.argv[1:]):
    args = parse_args(argv)

    # Do stuff here.

if __name__ == "__main__":
    main()
