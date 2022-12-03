# Advent of Code 2022

# Day 1

# Find the number of calories that is being carried
# by the elf with the most calories

with open('Day1/day1input.txt', 'r') as f:
    max_cals = [0,0,0]
    curr = 0
    while True:
        line = f.readline()

        if not line:
            break

        if line == "\n":
            max_cals.append(curr)
            max_cals = sorted(max_cals)
            max_cals.pop(0)
            curr = 0
        else:
            curr += int(line.strip())

    print(max_cals)
    print(sum(max_cals))