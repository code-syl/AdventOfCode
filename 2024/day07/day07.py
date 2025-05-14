def generateOperatorSets(length: int, base: int) -> list[list[int]]:
    # Cartesion product of sets of itself
    # Generate each possibility of a list of length N where items can be one of base options (duplicates allowed)
    result = []

    # for each 'length' positions there are 'base' options
    # so there are in total base^length possible options
    for i in range(base ** length): # 0 .. base^length-1
        combo = []
        value = i
        for _ in range(length): # 0 .. length-1
            digit = value % base # get the last digit
            combo.append(digit)
            value //= base # shift to the left 'base' digits

        result.append(combo)

    return result;

def solveable(equation: tuple[int, list[int]], operatorSets: list[list[int]] | None) -> bool:
    if operatorSets is None:
        return False

    # go through the each possible set of operators for each equation
    for i in range(len(operatorSets)):
        j = 0
        temp = equation[1][j]
        while j+1 < len(equation[1]):
            # 0 equals +, 1 equals *
            if operatorSets[i][j] == 0:
                temp = temp + equation[1][j+1]
            elif operatorSets[i][j] == 1:
                temp = temp * equation[1][j+1]
            else:
                temp = int(str(temp) + str(equation[1][j+1]))

            j += 1

        # if there is a match, it means the current equation is solveable
        if temp == equation[0]:
            return True

    return False

# parse input
calculations: list[tuple[int, list[int]]] = []
with open("input.real", "r") as file:
    for line in file:
        chunks = line.rstrip().split(": ")
        solution = int(chunks[0])
        numbers = [int(n) for n in chunks[1].split(" ")]
        calculations.append((solution, numbers))

# part 1
# get all possibilities where the numbers can be added and multiplied
# if the calculation ends up equalling the solution, then add to a sum
# calculations are always done from left to right!
solution = 0
cachedOperatorSets = dict()
for calc in calculations:
    # cache the operators if needed
    length = len(calc[1]) - 1
    if cachedOperatorSets.get(length) is None:
        cachedOperatorSets[length] = generateOperatorSets(length, 2)

    good = solveable(calc, cachedOperatorSets.get(length))
    if good:
        solution += calc[0]

print(f"Solution for part 1: {solution}")

# part 2
# There is a new operator, the concat operator!
# This combines the string value of each number, ex: 15 concat 6 == 156
# Rules from left to right still apply
solution = 0
cachedOperatorSets = dict()
for calc in calculations:
    # cache the operators if needed
    length = len(calc[1]) - 1
    if cachedOperatorSets.get(length) is None:
        cachedOperatorSets[length] = generateOperatorSets(length, 3)

    good = solveable(calc, cachedOperatorSets.get(length))
    if good:
        solution += calc[0]
        print(f"sol.: --> {solution}")

print(f"Solution for part 2: {solution}")
