elves_inventory = ""
current_elf = 0
elves = []

def load_input(input_file_path = "day1/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

elves_inventory = load_input()

for item in elves_inventory.splitlines():
    if len(elves) <= current_elf:
        elves.append(0)
    if item == "":
        current_elf += 1
        continue
    elves[current_elf] += int(item)

print("Answer1: {}".format(max(elves)))


elves.sort(reverse=True)
sum_first_tree = sum(elves[:3])
print("Answer2: {}".format(sum_first_tree))