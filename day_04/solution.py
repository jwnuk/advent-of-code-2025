import argparse

import numpy as np
from pathlib import Path


DEFAULT_PATH = "input.txt"


def solve_part1(grid: list):
    """
    The forklifts can only access a roll of paper (@) if there are fewer than four rolls
    of paper in the eight adjacent positions. If you can figure out which rolls of paper
    the forklifts can access, they'll spend less time looking and more time breaking
    down the wall to the cafeteria.
    """
    accessible_cnt = 0
    grid = [[char == "@" for char in line] for line in grid]
    arr = np.array(grid, dtype="bool")
    arr_pad = np.pad(arr, 1, constant_values=False)

    for i in range(1, arr.shape[0] + 1):
        for j in range(1, arr.shape[1] + 1):
            if_roll = arr_pad[i, j]

            if not if_roll:
                continue
            checked_arr = arr_pad[i - 1 : i + 2, j - 1 : j + 2]

            if checked_arr.sum() > 4:
                continue
            # print(i, j, if_roll)
            # print(checked_arr, f"\nSum: {checked_arr.sum()}\n")
            accessible_cnt += 1

    return accessible_cnt


def solve_part2(grid: list):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_PATH)
    raw = parser.parse_args().input.read_text()
    grid = raw.splitlines()

    print("Part 1:", solve_part1(grid))
    print("Part 2:", solve_part2(grid))


if __name__ == "__main__":
    main()
