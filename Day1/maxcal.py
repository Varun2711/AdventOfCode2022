# Advent of Code 2022

# Day 1

# Part 1
# Find the number of calories that is being carried
# by the elf with the most calories

# Part 2
# Find the total number of calories being carried
# by the top 3 most calorie carrying elves

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

    f.close()
