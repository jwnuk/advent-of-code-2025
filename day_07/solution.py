import argparse
from pathlib import Path

DEFAULT_PATH = "input.txt"


def solve_part1(diagram: list):
    """
    A tachyon beam enters the manifold at the location marked S; tachyon beams always
    move downward. Tachyon beams pass freely through empty space (.). However, if a
    tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon
    beam continues from the immediate left and from the immediate right of the splitter.
    Analyze your manifold diagram. How many times will the beam be split?
    """
    splits = 0
    beam_indices = [diagram[0].index("S")]

    for line in diagram[1:]:
        new_beams = set()
        indices_to_remove = set()
        # new_line = line

        for beam_ix in beam_indices:
            if line[beam_ix] == "^":
                new_beams.add(beam_ix - 1)
                new_beams.add(beam_ix + 1)
                indices_to_remove.add(beam_ix)
                splits += 1

        beam_indices = sorted(
            new_beams.union(beam_indices).difference(indices_to_remove)
        )
        # for ix in beam_indices:
        #     new_line = new_line[:ix] + "|" + new_line[ix + 1 :]
        # print(new_line)

    return splits


def solve_part2(diagram: list):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", default=DEFAULT_PATH, type=Path)
    raw = parser.parse_args().input.read_text()
    diagram = raw.split()

    print("Part 1:", solve_part1(diagram))
    # print("Part 2:", solve_part2(diagram))


if __name__ == "__main__":
    main()
