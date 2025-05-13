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

def traverse(grid: list[list[int]], startX: int, startY: int, part1: bool = True) -> tuple[int, set[tuple[int, int, int]]]:
    directions = [
        [0, -1], # North
        [1,  0], # East
        [0,  1], # South
        [-1, 0]  # West
    ] # % len(directions)
    x, y = startX, startY
    numberOfTurns = 0
    turns = set()

    # once the guard leaves the grid, their patrol is complete
    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        # move in the direction the guard is facing (% 4)
        direction = directions[numberOfTurns % len(directions)]
        nextX, nextY = x + direction[0], y + direction[1]

        # for part 2, raise an exception when you are looping
        # use a Set for performance (o(1) lookup)
        if nextX < 0 or nextX >= len(grid[0]) or nextY < 0 or nextY >= len(grid):
            break
        if (x, y, numberOfTurns % len(directions)) in turns:
            raise Exception("looping")

        nextSymbol = grid[nextY][nextX]
        # if there is an obstacle, turn clockwise once but don't move
        if nextSymbol == 1:
            numberOfTurns += 1
            continue

        turn = (x, y, numberOfTurns % len(directions))
        turns.add(turn)
        grid[y][x] = 2

        x, y = nextX, nextY

    grid[y][x] = 2 # mark last step

    if part1:
        return count(grid, 2), turns

    # do not count for the second part
    return 0, set()

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
solution, route = traverse(map, startX, startY)
print(f"Part 1 solution: {solution}")

# part 2
#
# get the route of part 1
# for each coordinate that is not the start point, place a wall
# check for an Exception
#   if yes, then add only the coordinates to the wall list
# count unique walls that caused a loop
walls = set()
for point in route:
    if point == (startX, startY, 0):
        continue
    try:
        # set one of the path's coords to a wall, then traverse
        map[point[1]][point[0]] = 1
        _, _ = traverse(map, startX, startY)
    except Exception:
        # if looping, add to the wall list
        walls.add((point[0], point[1]))
    finally:
        # reset the wall to a normal coordinate
        map[point[1]][point[0]] = 0

solution = len(walls)
print(f"Part 2 solution: {solution}")
