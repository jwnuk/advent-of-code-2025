import argparse
from pathlib import Path

DEFAULT_PATH = "input.txt"


def solve_part1(banks: list):
    """
    The batteries are arranged into banks; each line of digits in your input corresponds
    to a single bank of batteries. Within each bank, you need to turn on exactly two
    batteries; the joltage that the bank produces is equal to the number formed
    by the digits on the batteries you've turned on. For example, if you have a bank
    like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts.
    (You cannot rearrange batteries.)
    """
    jolts = []

    for bank in banks:
        first_digit = str(max([int(char) for char in bank[:-1]]))
        first_index = bank.find(first_digit)
        second_digit = str(max([int(char) for char in bank[first_index + 1 :]]))
        jolts_b = int(first_digit + second_digit)
        jolts.append(jolts_b)

    return sum(jolts)


def solve_part2(banks: list):
    """
    Now, you need to make the largest joltage by turning on exactly twelve batteries
    within each bank.

    The joltage output for the bank is still the number formed by the digits
    of the batteries you've turned on; the only difference is that now there will be
    12 digits in each bank's joltage output instead of two.
    """
    jolts = []

    for bank in banks:
        jolts_b = ""
        next_start = -1
        n = 1
        for i in range(11, 0, -1):
            current_start = next_start + 1
            bank_part = bank[current_start:-i]
            # print(f"Searching in {bank_part}, start: {current_start}, stop: {-i}")
            max_digit = str(max([int(char) for char in bank_part]))
            next_start = current_start + bank_part.find(max_digit)
            # print(f"iteration: {n}, max: {max_digit}, index: {next_start}\n")
            n += 1
            jolts_b += max_digit

        last_digit = str(max([int(char) for char in bank[next_start + 1 :]]))
        jolts_b += last_digit
        jolts.append(int(jolts_b))

    return sum(jolts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_PATH)
    raw = parser.parse_args().input.read_text()
    banks = raw.splitlines()

    print("Part 1:", solve_part1(banks))
    print("Part 2:", solve_part2(banks))


if __name__ == "__main__":
    main()
