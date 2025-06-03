# parse input
disk = ""
with open("input.real", "r") as file:
    disk = file.read().rstrip()
print(f"Compressed Disk Size: {len(disk)}")
# ------------------------------------------------------------
# checksum calculation
def checksum(disk: list[str]) -> int:
    i = 0
    sum = 0
    for block in disk:
        if block == ".":
            break
        value = int(block)
        sum += i * value
        i += 1

    return sum

# uncompress
def uncompress(compressed_disk: str) -> list[str]:
    uncompressed_disk = []
    id = 0
    is_file = True

    for block in compressed_disk:
        length = int(block)
        if is_file:
            uncompressed_disk.extend([str(id)] * length)
            id += 1
        else:
            uncompressed_disk.extend(["."] * length)
        is_file = not is_file

    return uncompressed_disk
# ------------------------------------------------------------
# part 1
uncompressed_disk = uncompress(disk)
print(f"Uncompressed Disk Size: {len(uncompressed_disk)}")

# reorder
i, j = 0, len(uncompressed_disk) - 1 # indices
while i < j:
    if uncompressed_disk[i] != ".":
        i += 1
        continue

    if uncompressed_disk[j] == ".":
        j -= 1
        continue

    uncompressed_disk[i] = uncompressed_disk[j]
    uncompressed_disk[j] = "."
    i += 1
    j -= 1

print("Checksum:", checksum(uncompressed_disk))
