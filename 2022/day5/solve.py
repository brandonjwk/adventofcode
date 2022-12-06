import sys
from copy import deepcopy
sys.path.insert(0, '/Users/bwakefield/workspace/aoc-2022')
from util.read_input import read_input

# input = read_input("day5/sample")
input = read_input("day5/input.txt")

def read_move(i):
    s = i.split(" ")
    m = int(s[1])
    f = int(s[3]) - 1
    t = int(s[5]) - 1

    return m, f, t 

for i in range(len(input)):
    if input[i].startswith(" 1"):
        b = i
        s = int(input[i][-3:])
        break

stacks = [[] for i in range(s)]
for i in reversed(range(b)):
    for j in range(s):
        c = input[i][j*4+1:j*4+2].rstrip()
        if c:
            stacks[j].append(c)

# print(stacks)
stacks_9001 = deepcopy(stacks)

for i in range(b+2,len(input)):
    moves, f, t = read_move(input[i])
    for m in range(moves):
        p = stacks[f].pop()
        stacks[t].append(p)
    
    stacks_9001[t] += stacks_9001[f][-1*moves:]
    stacks_9001[f] = stacks_9001[f][:-1*moves]

# print(stacks)
# print(stacks_9001)

part_1 = ""
part_2 = ""
for s in stacks:
   part_1 += s.pop()

for s in stacks_9001:
   part_2 += s.pop()

print(f"Part 1 = {part_1}")
print(f"Part 2 = {part_2}")
