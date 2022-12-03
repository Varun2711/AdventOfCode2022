# Day 3


# Find the sum of priorities of all the items
# that exist in both compartments of each rucksack

# Each string input is a rucksack
# each half of a string is a compartment of the rucksack
# items are denoted by the letters of the alphabet (case sensitive)
# items a-z take priorities 1-26 and A-Z take 27-52

def get_psum_for_badges(sacks):
    p_sum = 0
    for i in range(0, len(sacks), 3):
        for item in set(sacks[i]):
            if item in set(sacks[i+1]) and item in set(sacks[i+2]) and item != '\n':
                if item.isupper():
                    p_sum += ord(item) - 38
                else:
                    p_sum += ord(item) - 96
    print(p_sum)

with open("Day3/day3input.txt", "r") as f:
    rucksacks = f.readlines()
    p_sum = 0
    # Part 1 code
    for sack in rucksacks:
        split_idx = (len(sack)//2)
        c1, c2 = sack[0:split_idx], sack[split_idx::]
        for item in set(c1):
            if item in set(c2):
                if item.isupper():
                    p_sum = p_sum + ord(item) - 38
                else:
                    p_sum = p_sum + ord(item) - 96

    print(p_sum)
    get_psum_for_badges(rucksacks)
    f.close()