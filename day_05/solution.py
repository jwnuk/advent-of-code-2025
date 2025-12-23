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
    fresh_ids_arr = np.array([])

    for ids_range in ingredient_ids:
        start, stop = ids_range.split("-")
        range_arr = np.arange(int(start), int(stop) + 1)
        fresh_ids_arr = np.unique(np.concat([fresh_ids_arr, range_arr]))

    ingredient_list = [int(ingredient) for ingredient in ingredient_list]
    ingredient_arr = np.array(ingredient_list)
    fresh_ingredients = ingredient_arr[np.isin(ingredient_arr, fresh_ids_arr)]

    return fresh_ingredients.shape[0]


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
