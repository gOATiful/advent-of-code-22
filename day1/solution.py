elves_inventory = ""
current_elf = 0
elves = []

with open("day1/input.txt", "r") as input_file:
    elves_inventory = input_file.read()

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