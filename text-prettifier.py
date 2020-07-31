#! /usr/bin/env python3
# -*- coding: UTF-8 -*-


import argparse
import sys
from pathlib import Path


def optimal_split(s: list, max_len: int):
    current_len = len(s[0])
    if current_len > max_len:
        return (" ".join(s), None)

    for i, elem in enumerate(s[1:]):
        current_len += len(elem) + 1  # +1 for whitespaces
        if current_len > max_len:
            return (" ".join(s[:i]), " ".join(s[i:]))


def main(path_in, path_out, max_len):
    """Read a file"""
    with open(path_in, "r") as fin:
        with open(path_out, "w") as fout:
            for line in fin.readlines():
                string = line.rstrip()
                if len(string) > max_len:
                    left_str, right_str = optimal_split(string.split(), max_len)
                    fout.write("{}\n{}\n".format(left_str, right_str))
                else:
                    fout.write("{}\n".format(string))


def arg_parser():
    """The function to fill command line arguments and parse them"""
    parser = argparse.ArgumentParser(
        description="Calculate linear subspace weight spectrum."
        )

    parser.add_argument("input", help="a path to the input text file")
    parser.add_argument("output", help="a path to the output text file")
    parser.add_argument("max_length", type=int,
                        help="the maximum line length")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = arg_parser()
    main(Path(args.input), Path(args.output), args.max_length)
