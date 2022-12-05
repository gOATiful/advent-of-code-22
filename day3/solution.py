input_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def load_input(input_file_path = "day3/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

input_data = load_input()

def get_item_score(error):
  if error.islower():
    return ord(error) - ord('a') + 1
  return ord(error) - ord('A') + 27

errors_in_rucksack = []
scores_in_rucksack = []

for rucksack in input_data.splitlines():
  rucksack_size = len(rucksack)
  rucksack_delimiter = int(rucksack_size/2)
  left_c = rucksack[:rucksack_delimiter]
  right_c = rucksack[rucksack_delimiter:]
  for l in list(left_c):
    if l in list(right_c):
      errors_in_rucksack.append(l)
      scores_in_rucksack.append(get_item_score(l[0]))
      break

print("Answer1: {}".format(sum(scores_in_rucksack)))


elves = input_data.splitlines()

badges = []
for rucksack_idx in range(0, len(elves), 3):
  group_of_three = elves[rucksack_idx:rucksack_idx+3]
  badge = set(group_of_three[0]) & set(group_of_three[1]) & set(group_of_three[2])
  badges.extend(list(badge))

scores = [get_item_score(x) for x in badges]
print("Answer2: {}".format(sum(scores)))