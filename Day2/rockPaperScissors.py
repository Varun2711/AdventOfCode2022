# Day 2

# Need to optimize the choices of x, y, z in the second
# column for a rock paper scissors game strategy

# INFO: A: Rock, B: Paper, C: Scissors
# CANNOT win all rounds; it will raise suspicion
# The score for a round is calculated as following:
# score of your choice + score of your outcome
# scores of choice: Rock: 1, Paper: 2, Scissors: 3
# score of outcome: lose: 0, draw: 3, win: 6

# The dictionary for the opponent's choices
opp_choice_dict = {"A": "rock", "B": "paper", "C": "scissors"}

# The choice score dictionary
choice_score_dict = {"rock": 1, "paper": 2, "scissors": 3}

# Possible dictionary for your choice
strat1_dict = {"X": "rock", "Y": "paper", "Z": "scissors"}
strat2_dict = {"X": "paper", "Y": "scissors", "Z": "rock"}
strat3_dict = {"X": "scissors", "Y": "rock", "Z": "paper"}

def get_strat_score(strat, rounds):
    total_score = 0
    total_rounds = len(rounds)
    rounds_won = 0
    for round in rounds:
        round = round.split()
        score = get_score(strat[round[1]], opp_choice_dict[round[0]])
        if score > 6:
            rounds_won +=1
        total_score += score
    return (total_score, rounds_won/total_rounds)


def get_score(your_choice, opp_choice):
    if your_choice == opp_choice:
        return choice_score_dict[your_choice] + 3
    elif your_choice == 'rock' and opp_choice == 'scissors':
        return choice_score_dict[your_choice] + 6
    elif your_choice == 'paper' and opp_choice == 'rock':
        return choice_score_dict[your_choice] + 6
    elif your_choice == 'scissors' and opp_choice == "paper":
        return choice_score_dict[your_choice] + 6
    
    return choice_score_dict[your_choice]

# This function is for part 2
# Don't get tilted and write code like this because of a little mistake
# in the future
def get_elf_strat_score(rounds):
    total_score = 0
    total_rounds = len(rounds)
    rounds_won = 0

    for round in rounds:
        round = round.split()
        if round[1] == "X":
            if round[0] == "A":
                total_score += 3
            elif round[0] == "B":
                total_score += 1
            elif round[0] == "C":
                total_score += 2
        elif round[1] == "Y":
            if round[0] == "A":
                total_score += 4
            elif round[0] == "B":
                total_score += 5
            elif round[0] == "C":
                total_score += 6
        elif round[1] == "Z":
            rounds_won += 1
            if round[0] == "A":
                total_score += 8
            elif round[0] == "B":
                total_score += 9
            elif round[0] == "C":
                total_score += 7

    return (total_score, rounds_won/total_rounds)



with open("Day2/day2input.txt", 'r') as f:
    rounds = f.readlines()

    print(get_strat_score(strat1_dict, rounds))
    print(get_strat_score(strat2_dict, rounds))
    print(get_strat_score(strat3_dict, rounds))
    print(get_elf_strat_score(rounds))


    