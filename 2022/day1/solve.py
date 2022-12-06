import sys
sys.path.insert(0, '/Users/bwakefield/workspace/aoc-2022')
from util.read_input import read_input

# input = read_input("day1/sample")
input = read_input("day1/input.txt")

cal = 0
elf = 0
m = 0
elves = []
for i in input:
    if i == '':
        # print(f"Elf {elf} has {m} calories")
        if m > cal:
            cal = m
        elves.append(m)
        elf += 1
        m = 0
        continue

    m += int(i)

# print(f"Elf {elf} has {m} calories")
if m > cal:
    cal = m
elves.append(m)

top = sum(sorted(elves)[-3:])

print(f"Part 1 = {cal}")
print(f"Part 2 = {top}")
