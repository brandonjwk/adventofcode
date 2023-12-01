import sys
sys.path.insert(0, ".")
from util.read_input import read_input

# input = read_input("day1/sample")
input = read_input("day1/input")

def find_digit(s):
  for c in s:
    if c.isdigit():
      return c

def word2numsub(i):
  map = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
  }

  j = 0; w = 3; r = i
  # Scanning loop
  while j+w <= len(i):
    # Increasing window size loop
    while j+w <= len(i):
      s = i[j:j+w]
      if s in map:
        # print(f"Found substition in {s} in {i}")s
        return i[0:j] + map[s] + i[j+w:]
      w += 1

      if w > 5:
        # Escape early if word is too long
        continue

    j += 1; w = 3
  
  # print("No further substituons")
  return i


part1 = 0
for i in input:
  cal = int(find_digit(i) + find_digit(reversed(i)))
  # print(cal)
  part1 += cal

print("Part 1", part1)


part2 = 0
for i in input:
  # print(f"Processing line {i}")
  p = i; n = word2numsub(p)
  while p != n:
    p = n
    n = word2numsub(p)
  # print(f"Completed substitions.. Result: {n}")

  cal = int(find_digit(n) + find_digit(reversed(n)))
  # print(cal)
  part2 += cal

print("Part 2", part2)
