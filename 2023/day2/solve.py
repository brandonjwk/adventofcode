import sys
sys.path.insert(0, '.')
from util.read_input import read_input

import math

# input = read_input("day2/sample")
input = read_input("day2/input")

game_config = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def isvalidvalue(cube,val):
  if val > game_config[cube]:
    return False

  return True

def isvaliddraw(draw):
  cubesets = draw.split(",")
  for c in cubesets:
    cube, val = parsecubeset(c)
    if not isvalidvalue(cube,val):
      return False

  return True

def parsecubeset(cubeset):
    cubeset = cubeset.strip()
    val = int(cubeset.split(" ")[0])
    cube = cubeset.split(" ")[1]
    return cube, val

def isvalidgame(draws):
  for d in draws:
    if not isvaliddraw(d):
      return False

  return True

def makevalidconfig(draws):
  config = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for d in draws:
    cubesets = d.split(",")
    for c in cubesets:
      cube, val = parsecubeset(c)
      if val > config[cube]:
        config[cube] = val
  
  return config

def gamepower(draws):
  config = makevalidconfig(draws)
  return math.prod(config.values())

part1 = 0; part2 = 0
for i in input:
  n = int(i.split(":")[0].split(" ")[1])
  draws = i.split(":")[1].split(";")
  # print(draws)

  if isvalidgame(draws):
    part1 += n
  
  part2 += gamepower(draws)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
