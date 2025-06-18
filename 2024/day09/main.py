# parse input
disk = ""
with open("input.real", "r") as file:
    disk = file.read().rstrip()
print("Compressed Disk Size:", len(disk))
# ------------------------------------------------------------
# checksum calculation
def checksum(disk: list[int]) -> int:
    return sum(i * value for i, value in enumerate(disk) if value >= 0)

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

n = len(uncompressed_disk)
file_blocks = {}

# identify the files and positions
for i, value in enumerate(uncompressed_disk):
    if value >= 0:
        file_blocks.setdefault(value, []).append(i)

# precompute free space
free_spans = []
i = 0
while i < n:
    if uncompressed_disk[i] == -1:
        start = i
        while i < n and uncompressed_disk[i] == -1:
            i += 1
        free_spans.append((start, i - 1))
    else:
            i += 1

for file_id in sorted(file_blocks.keys(), reverse=True):
    positions = file_blocks[file_id]
    length = len(positions)
    file_start = positions[0]
    print("Processing ID:\t", file_id)

    for span_start, span_end in free_spans:
        span_length = span_end - span_start + 1
        if span_length >= length and span_start + length - 1 < file_start:
            # move
            for position in positions:
                uncompressed_disk[position] = -1
            for j in range(length):
                uncompressed_disk[span_start + j] = file_id

            # update file blocks
            file_blocks[file_id] = list(range(span_start, span_start + length))

            # shrink
            if span_length == length:
                free_spans.remove((span_start, span_end))
            else:
                free_spans.remove((span_start, span_end))
                free_spans.append((span_start + length, span_end))
                free_spans.sort()

            break

solution = checksum(uncompressed_disk)
print(solution)
