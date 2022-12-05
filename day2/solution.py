input_data = """A Y
B X
C Z"""


select_score = {
    'X': 1,
    "Y": 2,
    "Z": 3
}

outcome_scoring = {
    'Z': 6,
    'Y': 3,
    'X': 0
} 

rules = {
    ('A', 'X') : 3,
    ('A', 'Y') : 6,
    ('A', 'Z') : 0,
    ('B', 'X') : 0,
    ('B', 'Y') : 3,
    ('B', 'Z') : 6,
    ('C', 'X') : 6,
    ('C', 'Y') : 0,
    ('C', 'Z') : 3
}


with open("day2/input.txt", "r") as input_file:
    input_data = input_file.read()

outcomes = []
for round in input_data.splitlines():
    round_split = round.split(" ")
    opponent_pick = round_split[0]
    my_pick = round_split[1]
    pick_score = select_score[my_pick]
    outcome = rules[(opponent_pick, my_pick)]
    outcomes.append(pick_score + outcome)

print("Answer1: {}".format(sum(outcomes)))


# A Rock
# B Paper
# C Scissors


# X lose
# Y draw
# Z win

# X Rock
# Y Paper
# Z Scissors
rules_part2 = {
    ('A', 'X') : 'Z',
    ('A', 'Y') : 'X',
    ('A', 'Z') : 'Y',
    ('B', 'X') : 'X',
    ('B', 'Y') : 'Y',
    ('B', 'Z') : 'Z',
    ('C', 'X') : 'Y',
    ('C', 'Y') : 'Z',
    ('C', 'Z') : 'X'
}

round_scores = []

for round in input_data.splitlines():
    round_split = round.split(" ")
    opponent_pick = round_split[0]
    outcome = round_split[1]
    outcome_points = outcome_scoring[outcome]
    select_points = select_score[rules_part2[(opponent_pick, outcome)]]
    round_scores.append(outcome_points + select_points)

print("Answer2: {}".format(sum(round_scores)))