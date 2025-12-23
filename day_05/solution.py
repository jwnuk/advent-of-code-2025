import argparse
import numpy as np
from pathlib import Path

DEFAULT_PATH = "input.txt"


def solve_part1(ingredient_ids: list, ingredient_list: list):
    """
    The database operates on ingredient IDs. It consists of a list of fresh ingredient
    ID ranges, a blank line, and a list of available ingredient IDs.
    The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4,
    and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is
    in any range.
    Process the database file from the new inventory management system.
    How many of the available ingredient IDs are fresh?
    """
    fresh_ingredients = 0

    ranges = [
        [int(ids_range.split("-")[0]), int(ids_range.split("-")[1])]
        for ids_range in ingredient_ids
    ]

    for ingredient_id in ingredient_list:
        ingredient_id_int = int(ingredient_id)
        if any(
            ingredient_id_int >= id_range[0] and ingredient_id_int <= id_range[1]
            for id_range in ranges
        ):
            fresh_ingredients += 1

    return fresh_ingredients


def solve_part2():
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default=DEFAULT_PATH, type=Path)
    raw = parser.parse_args().input.read_text()
    ingredient_ids, ingredient_list = [text.splitlines() for text in raw.split("\n\n")]

    print("Part 1:", solve_part1(ingredient_ids, ingredient_list))
    # print("Part 2:", solve_part2(ingredient_ids, ingredient_list))


if __name__ == "__main__":
    main()
