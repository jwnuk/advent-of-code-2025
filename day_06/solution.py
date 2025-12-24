import argparse
import numpy as np
from pathlib import Path

DEFAULT_PATH = "input.txt"


def solve_part1(worksheet: list):
    """
    Cephalopod math doesn't look that different from normal math. The math worksheet
    (your puzzle input) consists of a list of problems; each problem has a group of
    numbers that need to be either added (+) or multiplied (*) together.
    What is the grand total found by adding together all of the answers to the
    individual problems?
    """
    grand_total = 0
    worksheet = np.array(worksheet).transpose().tolist()

    for problem in worksheet:
        numbers = [int(a) for a in problem[:-1]]
        operation = problem[-1]
        line_total = numbers[0]
        i = 1
        while i < len(numbers):
            line_total = (
                line_total + numbers[i] if operation == "+" else line_total * numbers[i]
            )
            i += 1
        grand_total += line_total

    return grand_total


def solve_part2(worksheet: list):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default=DEFAULT_PATH, type=Path)
    raw = parser.parse_args().input.read_text()
    worksheet = [line.split() for line in raw.splitlines()]

    print("Part 1:", solve_part1(worksheet))
    # print("Part 2:", solve_part2(worksheet))


if __name__ == "__main__":
    main()
