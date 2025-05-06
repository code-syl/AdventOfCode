def characterToInt(character):
    if type(character) != str:
        return 404

    match character:
        case ".": return 0;
        case "#": return 1;
        case "^": return 9;
        case _: return 404;

# parse input
cardinalDirections = 4
map = []
with open("input.example", "r") as file:
    for line in file:
        line = line.rstrip()
        row = [characterToInt(c) for c in line]
        map.append(row)

print(map)
