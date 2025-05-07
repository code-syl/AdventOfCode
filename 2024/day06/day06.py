#!/usr/bin/env python3

def characterToInt(character: str) -> int:
    if type(character) != str:
        return 404

    match character:
        case ".": return 0;
        case "#": return 1;
        case "^": return 9;
        case _: return 404;

def find(grid: list[list[int]], n: int) -> tuple[int, int]:
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if grid[y][x] == n:
                return x, y
    raise Exception(f"integer {n} not found in grid!")

def count(grid: list[list[int]], n: int) -> int:
    count = 0
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if grid[y][x] == n:
                count += 1
    return count

# parse input
directions = [
    [0, -1], # North
    [1, 0],  # East
    [0, 1],  # South
    [-1, 0]  # West
] # % len(directions)
map = []
with open("input.real", "r") as file:
    for line in file:
        line = line.rstrip()
        row = [characterToInt(c) for c in line]
        map.append(row)

# part 1
# start traversing within bounds, keeping track of the number of turns
# turn when you encounter an obstacle '1'
# mark each previous step you take with '2'
# count the distinct steps
# keep moving and turning until you move out of bounds
x, y = find(map, 9)
numberOfTurns = 0
while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
    direction = directions[numberOfTurns % len(directions)]
    nextX, nextY = x + direction[0], y + direction[1]
    if nextX < 0 or nextX >= len(map[0]) or nextY < 0 or nextY >= len(map):
        break

    nextSymbol = map[nextY][nextX]
    if nextSymbol == 1:
        numberOfTurns += 1
        continue

    map[y][x] = 2
    x, y = nextX, nextY
map[y][x] = 2 # mark last step

print(f"Part 1 solution: {count(map, 2)}")
