import sys
sys.path.insert(0, '.')
from util.read_input import read_input

# input = read_input("day3/sample")
input = read_input("day3/input")


def is_symbol(c):
  charset = "[@_!#$%^&*()<>?/\|}{~:]+-="
  if c in charset:
    return True

  return False

def has_adjacent_symbol(input, pos):
  x = pos[0]; y = pos[1]
  
  # Check left
  if x-1 > 0:
    if is_symbol(input[y][x-1]):
      return True

  # Check top left
  if (x-1 > 0) and (y-1 > 0):
    if is_symbol(input[y-1][x-1]):
      return True

  # Check top
  if y-1 > 0:
    if is_symbol(input[y-1][x]):
      return True

  # Check top right
  if (x+1 < len(input[0])) and (y-1 > 0):
    if is_symbol(input[y-1][x+1]):
      return True

  # Check right
  if x+1 < len(input[0]):
    if is_symbol(input[y][x+1]):
      return True

  # Check bottom right
  if (x+1 < len(input[0])) and (y+1 < len(input)):
    if is_symbol(input[y+1][x+1]):
      return True

  # Check bottom
  if y+1 < len(input):
    if is_symbol(input[y+1][x]):
      return True
    
  # Check bottom left
  if (x-1 > 0) and (y+1 < len(input)):
    if is_symbol(input[y+1][x-1]):
      return True

  return False

def ispart(input, start_x, end_x, y):
  # check adjacent
  for x in range(start_x, end_x+1):
    pos=[x,y]
    # print(f"Processing {input[y][x]} at x={x}, y={y}...")
    if has_adjacent_symbol(input, pos):
      # print("Found adjacent symbol")
      return True

  return False

part_1 = 0
for y in range(len(input)):
  part_pos=[]
  for x in range(len(input[y])):
    c = input[y][x]
    # Flush buffer and check for part
    if not c.isdigit() and part_pos:
      part_num = int(input[y][part_pos[0]:part_pos[-1]+1])
      # print(f"Checking part number {part_num}")
      p = ispart(input, part_pos[0], part_pos[-1], y)
      # print(f"Val {p}")
      if p:
        part_1 += part_num

      part_pos=[]
    
    if c.isdigit():
      part_pos.append(x)

  # Flush buffer and check for part
  if part_pos:
    part_num = int(input[y][part_pos[0]:part_pos[-1]+1])
    # print(f"Checking part number {part_num}")
    p = ispart(input, part_pos[0], part_pos[-1], y)
    # print(f"Val {p}")
    if p:
      part_1 += part_num

print(f"Part 1: {part_1}")
