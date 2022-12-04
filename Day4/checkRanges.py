# Day 4

# Find the number of assignment pairs in which one range contains the other



with open("Day4/day4input.txt", "r") as f:
    pairs = [line.strip().split(",") for line in f.readlines()]
    pairs = [[a_range.split('-') for a_range in pair] for pair in pairs]

    # Part 1 and part 2
    count = 0
    for pair in pairs:
        r1 = pair[0]
        r2 = pair[1]

        r1[0] = int(r1[0])
        r2[0] = int(r2[0])

        r1[1] = int(r1[1])
        r2[1] = int(r2[1])

        if ((r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1])
         or (r1[1] in range(r2[0], r2[1])) or (r2[1] in range(r1[0], r1[1]))):
            count += 1


    print(count)


