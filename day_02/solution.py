import argparse
import numpy as np
from pathlib import Path

DEFAULT_INPUT = Path("input.txt")


def solve_part1(ranges: list):
    """
    Since the young Elf was just doing silly patterns, you can find the invalid IDs
    by looking for any ID which is made only of some sequence of digits repeated twice.
    So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

    What do you get if you add up all of the invalid IDs?
    """

    invalid_ids_all = []

    for id_range in ranges:
        id_min, id_max = id_range.split("-")
        divisor_min = int("1" + round((len(id_min) + 0.01) / 2) * "0")
        divisor_max = int("1" + round((len(id_max) + 0.01) / 2) * "0")
        id_min, id_max = int(id_min), int(id_max)

        ids_arr = np.arange(id_min, id_max + 1, 1)
        ids_processed = ids_arr // divisor_min
        ids_processed = np.unique(ids_processed)
        ids_processed = ids_processed * divisor_min + ids_processed

        if divisor_min != divisor_max:
            ids_processed_2 = ids_arr // divisor_max
            ids_processed_2 = np.unique(ids_processed_2)
            ids_processed_2 = ids_processed_2 * divisor_max + ids_processed_2
            ids_processed = np.append(ids_processed, ids_processed_2, axis=0)

        ids_invalid = ids_arr[np.isin(ids_arr, ids_processed)]
        ids_invalid_list_str = [str(id) for id in ids_invalid if len(str(id)) % 2 == 0]
        ids_invalid_list = [
            int(id) for id in ids_invalid_list_str if id[: int(len(id) / 2)] * 2 == id
        ]
        invalid_ids_all.extend(ids_invalid_list)

    invalid_ids_all_filtered = [id for id in invalid_ids_all if len(str(id)) % 2 == 0]

    return sum(invalid_ids_all_filtered)


def solve_part2(ranges: list):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, default=DEFAULT_INPUT)
    raw = parser.parse_args().input.read_text()
    ranges = raw.split(",")

    print("Part 1:", solve_part1(ranges))
    print("Part 2:", solve_part2(ranges))


if __name__ == "__main__":
    main()
