# parse input
from dataclasses import dataclass


disk = ""
with open("input.example", "r") as file:
    disk = file.read().rstrip()
print("Compressed Disk Size:", len(disk))
# ------------------------------------------------------------
# checksum calculation
def checksum(disk: list[int]) -> int:
    i = 0
    sum = 0
    for block in disk:
        if block == -1:
            continue
        value = int(block)
        sum += i * value
        i += 1

    return sum

# uncompress
def uncompress(compressed_disk: str) -> list[int]:
    uncompressed_disk = []
    id = 0
    is_file = True

    for block in compressed_disk:
        length = int(block)
        if is_file:
            uncompressed_disk.extend([id] * length)
            id += 1
        else:
            uncompressed_disk.extend([-1] * length)
        is_file = not is_file

    return uncompressed_disk
# ------------------------------------------------------------
# part 1
uncompressed_disk = uncompress(disk)
print("\nPart 1")
print("Uncompressed Disk Size:", len(uncompressed_disk))

# reorder
i, j = 0, len(uncompressed_disk) - 1 # indices
while i < j:
    if uncompressed_disk[i] != -1:
        i += 1
        continue

    if uncompressed_disk[j] == -1:
        j -= 1
        continue

    uncompressed_disk[i] = uncompressed_disk[j]
    uncompressed_disk[j] = -1
    i += 1
    j -= 1

print("Checksum:", checksum(uncompressed_disk))
# ------------------------------------------------------------
# part 2
print("\nPart2")
uncompressed_disk = uncompress(disk)
print("Uncompressed Disk Size:", len(uncompressed_disk))
print(uncompressed_disk)
