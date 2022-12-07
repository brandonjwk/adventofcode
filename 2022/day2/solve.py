import sys
sys.path.insert(0, '.')
from util.read_input import read_input

# input = read_input("day2/sample")
input = read_input("day2/input.txt")

to_shape = {"A":"ROCK","B":"PAPER","C":"SCISSORS","X":"ROCK","Y":"PAPER","Z":"SCISSORS"}
to_win = {"ROCK":"PAPER","PAPER":"SCISSORS","SCISSORS":"ROCK"}
to_loss = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"}
to_score = {"ROCK":1,"PAPER":2,"SCISSORS":3}

def select(a,o):
    if o == "X":
        b = to_loss[a]
    
    if o == "Y":
        b = a

    if o == "Z":
        b = to_win[a]

    return b

def score(a,b):
    shape_score = to_score[b]
    # Draw
    if a == b:
        return 3 + shape_score

    # Win
    if (
        (a=="ROCK" and b=="PAPER")
        or (a=="PAPER" and b=="SCISSORS")
        or (a=="SCISSORS" and b=="ROCK")
    ):
        return 6 + shape_score
    
    # Loss
    return 0 + shape_score

total = 0
for i in input:
    a = to_shape[i[0]]
    o = i[2]
    # b = to_shape[o] # part 1
    b = select(a,o)
    s = score(a,b)
    # print(f"Round:Opponent used {a}, Player used {b}, Score {s}")
    total += s

print(f"Part 1 = {total}")
# print(f"Part 2 = {top}")
