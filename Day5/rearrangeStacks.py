# Day 5

# Do stuff lol and get help from friends from time to time

with open("Day5/day5input.txt", "r") as f:
    data = f.readlines()

    stacks_data = data[0:8]
    stacks_data = [level.strip() for level in stacks_data]

    stacks = [[],[],[],[],[],[],[],[],[]]

    levels = []

    for level in stacks_data:
        temp = level
        for i in range(0, len(temp), 4):
            if temp[i] == " ":
                temp = temp[0:i] + "[.]" + temp[i+3::]
        levels.append(temp)

    for level in levels:
        level = level.split()
        for i in range(len(level)):
            if level[i] != "[.]":
                stacks[i].append(level[i])
    
    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]


    rearrange_data = data[10::]

    for line in rearrange_data:
        line = line.split()
        count, src, dst = int(line[1]), int(line[3])-1, int(line[5])-1

        temp = []
        for i in range(count):
            temp.append(stacks[src].pop())
        
        stacks[dst] = stacks[dst] + temp[::-1] 

    for stack in stacks: print(stack)