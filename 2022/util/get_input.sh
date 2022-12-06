#!/bin/zsh

DAY=$1
SESSION=$(cat .session)

DAY_URL="https://adventofcode.com/2022/day/${DAY}"
INPUT_PATH="day${DAY}/input.txt"
curl -fsSL --cookie session=$SESSION "$DAY_URL/input" -o $INPUT_PATH
