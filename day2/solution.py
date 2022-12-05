input_data = """A Y
B X
C Z"""


select_score = {
    'X': 1,
    "Y": 2,
    "Z": 3
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


rules_part2 = {
    ('A', 'X') : 'Z',
    ('A', 'Y') : 'X',
    ('A', 'Z') : 'Y',
    ('B', 'X') : 'Z',
    ('B', 'Y') : 'Y',
    ('B', 'Z') : 'X',
    ('C', 'X') : 'Y',
    ('C', 'Y') : 'Z',
    ('C', 'Z') : 'X'
}

outcome_scores = []

for round in input_data.splitlines():
    round_split = round.split(" ")
    opponent_pick = round_split[0]
    outcome = round_split[1]
    print(rules_part2[(opponent_pick, outcome)])