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

def traverse(grid: list[list[int]], startX: int, startY: int) -> int:
    directions = [
        [0, -1], # North
        [1,  0], # East
        [0,  1], # South
        [-1, 0]  # West
    ] # % len(directions)
    x, y = startX, startY
    numberOfTurns = 0

    # once the guard leaves the grid, their patrol is complete
    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        # move in the direction the guard is facing (% 4)
        direction = directions[numberOfTurns % len(directions)]
        nextX, nextY = x + direction[0], y + direction[1]
        if nextX < 0 or nextX >= len(grid[0]) or nextY < 0 or nextY >= len(grid):
            break

        nextSymbol = grid[nextY][nextX]
        # if there is an obstacle, turn clockwise once but don't move
        if nextSymbol == 1:
            numberOfTurns += 1
            continue

        grid[y][x] = 2
        x, y = nextX, nextY
    grid[y][x] = 2 # mark last step

    return count(grid, 2)

# parse input
map = []
with open("input.real", "r") as file:
    for line in file:
        map.append([characterToInt(c) for c in line.rstrip()])

# part 1
# start traversing within bounds, keeping track of the number of turns
# turn when you encounter an obstacle '1'
# mark each previous step you take with '2'
# count the distinct steps
# keep moving and turning until you move out of bounds
startX, startY = find(map, 9)
solution = traverse(map, startX, startY)
assert solution == 5551, "incorrect answer for part 1"
print(f"Part 1 solution: {solution}")

# part 2
# reset starting position
# get all positions of the guard's original path
# make copy of map
# try and change one coordinate each time to an obstacle
# traverse and check if it is a loop
# (might want to make function of part1 and add looping check...
# ...by keeping track of the already traversed coordinates + directions...
# ...if the same coordinate + direction occurs, it is a loop, then raise Error)
map[startY][startX] = 9
