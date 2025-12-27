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


def solve_part2(worksheet_lines: list):
    """
    Cephalopod math is written right-to-left in columns. Each number is given in its own
    column, with the most significant digit at the top and the least significant digit
    at the bottom. (Problems are still separated with a column consisting only of
    spaces, and the symbol at the bottom of the problem is still the operator to use.)
    Solve the problems on the math worksheet again. What is the grand total found by
    adding together all of the answers to the individual problems?
    """
    grand_total = 0
    number_lines = worksheet_lines[:-1]
    operations_list = worksheet_lines[-1].split()
    line_len = max([len(line) for line in worksheet_lines])
    memory = []

    for j in range(line_len - 1, -1, -1):
        current_number = "".join([line[j] for line in number_lines]).strip()

        try:
            memory.append(int(current_number))
            # print(memory)
        except ValueError:
            pass

        if current_number == "" or j == 0:
            operation = operations_list.pop(-1)
            # print(operation)
            line_total = memory[0]
            i = 1
            while i < len(memory):
                line_total = (
                    line_total + memory[i]
                    if operation == "+"
                    else line_total * memory[i]
                )
                i += 1
            grand_total += line_total
            memory = []

    return grand_total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default=DEFAULT_PATH, type=Path)
    raw = parser.parse_args().input.read_text()
    worksheet_lines = raw.splitlines()
    worksheet = [line.split() for line in worksheet_lines]

    print("Part 1:", solve_part1(worksheet))
    print("Part 2:", solve_part2(worksheet_lines))


if __name__ == "__main__":
    main()
