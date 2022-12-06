import sys
from copy import deepcopy
sys.path.insert(0, '/Users/bwakefield/workspace/aoc-2022')
from util.read_input import read_input

# input = read_input("day6/sample")
input = read_input("day6/input.txt")

buffer = list(input[0])
part_1 = 0
for i in range(4,len(buffer)):
    if len(set(buffer[i-4:i])) == 4:
        part_1 = i
        break

part_2 = 0
for i in range(14,len(buffer)):
    if len(set(buffer[i-14:i])) == 14:
        part_2 = i
        break

print(f"Part 1 = {part_1}")
print(f"Part 2 = {part_2}")