from dataclasses import dataclass
from collections import defaultdict
import itertools

@dataclass
class Coordinate:
    x: int
    y: int
    frequency: str

# parse input
antennas = defaultdict(list)
bounds = Coordinate(0, 0, "")
with open("input.real", "r") as file:
    x_bounds = 0
    y = 0
    for line in file:
        x = 0
        line = line.rstrip()
        if len(line) - 1 > x_bounds:
            x_bounds = len(line) - 1
        for point in line:
            if point != ".":
                antennas[point].append(Coordinate(x, y, point))
            x += 1
        y += 1
    bounds.x = x_bounds
    bounds.y = y - 1

# part 1
antinodes = set()
for frequency in antennas.keys():
    # get lines between antennas
    combinations = list(itertools.combinations(antennas[frequency], 2))
    # frequencies with only 1 antenna do not create antinodes
    if (len(combinations) < 2):
        continue
    for combination in combinations:
        A, B = combination[0], combination[1]
        # extend the line between the antennas by the distance between
        # the extended coordinates equal the antinodes
        dx = B.x - A.x
        dy = B.y - A.y
        antinode1 = Coordinate(B.x + dx, B.y + dy, "")
        antinode2 = Coordinate(A.x - dx, A.y - dy, "")
        # bounds check for both antinodes
        if 0 <= antinode1.x <= bounds.x and 0 <= antinode1.y <= bounds.y:
            antinodes.add((antinode1.x, antinode1.y))
        if 0 <= antinode2.x <= bounds.x and 0 <= antinode2.y <= bounds.y:
            antinodes.add((antinode2.x, antinode2.y))
print("day 8 part 1 solution: ", len(antinodes))
