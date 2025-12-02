import argparse
from pathlib import Path

DEFAULT_INPUT = Path("input.txt")


def solve_part1(rotations: list):
    position = 50
    zero_cnt = 0

    for rotation in rotations:
        # print("MOVE:", rotation)
        direction = rotation[0]
        move = int(rotation[1:])
        hundreds = 0

        if direction == "L":
            move = -move

        position += move

        if position > 99:
            hundreds = position // 100
        elif position < 0:
            hundreds = position // 100

        position -= 100 * hundreds
        zero_cnt += int(position == 0)
        # print("UPDATED:", position, "\n")

    return zero_cnt


def solve_part2(rotations: list):
    position = 50
    zero_cnt = 0

    for rotation in rotations:
        # print("MOVE:", rotation)
        starting_position = position
        direction = rotation[0]
        move = int(rotation[1:])

        if direction == "L":
            move = -move

        position += move

        while position > 100:
            # print("over, rotated, ADDED")
            position -= 100
            zero_cnt += 1
        if position == 100:
            position -= 100

        if position < 0 and starting_position == 0:
            # print("0 at start, SUBSTRACTED")
            zero_cnt -= 1
        while position < 0:
            # print("below, rotated, ADDED")
            position += 100
            zero_cnt += 1

        zero_cnt += int(position == 0)
        # print("ADDED") if int(position == 0) else True
        # print("UPDATED:", position, zero_cnt, "\n")

    return zero_cnt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_INPUT)
    raw = parser.parse_args().input.read_text()
    rotations = raw.splitlines()

    print("Part 1:", solve_part1(rotations))
    print("Part 2:", solve_part2(rotations))


if __name__ == "__main__":
    main()
