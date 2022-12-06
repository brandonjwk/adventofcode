import sys
sys.path.insert(0, '/Users/bwakefield/workspace/aoc-2022')
from util.read_input import read_input

# input = read_input("day4/sample")
input = read_input("day4/input.txt")

def get_assignment(s):
    x = s.split("-")
    return set(range(int(x[0]),int(x[1])+1))

def is_contains(a,b):
    if a.issubset(b) or b.issubset(a):
        return True
    
    return False

def is_overlap(a,b):
    if len(a.intersection(b)) == 0:
        return False
    
    return True

part_1 = 0
part_2 = 0
for i in input:
    s = i.split(",")
    a = get_assignment(s[0])
    b = get_assignment(s[1])
    t = is_contains(a,b)
    # print(f"{i} is {t}")
    if t:
        part_1 += 1
    
    r = is_overlap(a,b)
    # print(f"{i} is {r}")
    if r:
        part_2 += 1

print(f"Part 1 = {part_1}")
print(f"Part 2 = {part_2}")
