#!/usr/bin/env python3

import math

def check(sequence, applicableRules):
    for rule in applicableRules:
        if not (sequence.index(rule[0]) < sequence.index(rule[1])):
            return False

    return True

# setup
secondInput = False
rules = []
sequences = []

with open("input.real", "r") as file:
    for line in file:
        if line.rstrip() == "":
            secondInput = True
            continue
        match secondInput:
            case False:
                rules.append(list(map(int, line.rstrip().split("|"))))
            case True:
                sequences.append(list(map(int, line.rstrip().split(","))))

# part 1
correctSequences = []
incorrectSequences = [] # for part 2
for sequence in sequences:
    correct = True
    for rule in rules:
        # check if rule applies to sequence
        # rule applies if both first and second are present in sequence
        # if the rule does not apply, then disregard and continue
        if not (rule[0] in sequence and rule[1] in sequence):
            continue

        # check if first number in rule appears before second number
        # if this is not the case, flip the flag and stop checking the sequence
        if not (sequence.index(rule[0]) < sequence.index(rule[1])):
            correct = False
            incorrectSequences.append(sequence)
            break

    if correct:
        correctSequences.append(sequence)

sum = 0
for sequence in correctSequences:
    sum += sequence[math.floor(len(sequence) / 2)]

print(f"Part 1 answer: {sum}")

# part 2
correctedSequences = []
for sequence in incorrectSequences:
    applicableRules = []
    for rule in rules:
        if (rule[0] in sequence and rule[1] in sequence):
            applicableRules.append(rule)

    while not check(sequence, applicableRules):
        for rule in applicableRules:
            idx1 = sequence.index(rule[0])
            idx2 = sequence.index(rule[1])
            if idx1 < idx2:
                continue

            sequence[idx1], sequence[idx2] = sequence[idx2], sequence[idx1]

    correctedSequences.append(sequence)

sum = 0
for sequence in correctedSequences:
    sum += sequence[math.floor(len(sequence) / 2)]

print(f"Part 2 answer: {sum}")
