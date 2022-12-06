# Day 6

# Need to find how many characters have passed before the 
# appearance of the first marker from the datastream

# Note: a marker is a string of last 4 characters at the given period. 
# A valid marker will only contain unique characters

def check_marker(marker):
    return len(marker) == len(set(marker))

with open("Day6/day6input.txt", "r") as f:
    data = f.readlines()

    for i in range(13, len(data[0])):
        marker_cand = data[0][i-13: i+1]
        if check_marker(marker_cand):
            print(i+1)
            break
