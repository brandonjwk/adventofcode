import sys
sys.path.insert(0, '.')
from util.read_input import read_input

# input = read_input("day3/sample")
input = read_input("day3/input.txt")

def priority(c):
    p = ord(c.lower()) - 96
    if c.isupper():
        p += 26
    
    return p

part_1 = 0
for i in input:
    m = len(i)//2
    c = set(i[:m]).intersection(set(i[m:])).pop()
    part_1 += priority(c)

part_2 = 0
for i in range(0,len(input),3):
    c = (set(input[i]) & set(input[i+1]) & set(input[i+2])).pop()
    part_2 += priority(c)

print(f"Part 1 = {part_1}")
print(f"Part 2 = {part_2}")
