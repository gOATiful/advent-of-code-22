
input_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

chars_per_container = 4

def load_input(input_file_path = "day5/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

def parse_stacks(input: str):
    lines = input.splitlines()
    stack_cnt = int((len(lines[-1]) +1) / chars_per_container)
    lines.reverse()
    stacks = [[] for x in range(stack_cnt)]
    for line in lines[1:]:
        for i in range(stack_cnt):
            container = line[chars_per_container * i + 1]
            if container != " ":
              stacks[i].insert(0, container)
    return stacks

def parse_instructions(input: str):
  import re
  regex = re.compile(r"(.*?)\s(\d+).*?(\d+).*?(\d+)")
  instructions = []
  for line in input.splitlines():
    matches = re.match(regex, line)
    amount = int(matches.group(2))
    from_stack =  int(matches.group(3))
    to_stack =  int(matches.group(4))
    instructions.append((amount, from_stack, to_stack))
  return instructions

def instruction_move_9000(stacks, amount, from_stack, to_stack):
  for _ in range(amount):
    container_from = stacks[from_stack-1].pop(0)
    stacks[to_stack-1].insert(0, container_from)
  return stacks

def get_top_containers(stacks):
  top_containers = ""
  for stack in stacks:
    if len(stack) > 0:
      top_containers += stack[0]
  return top_containers

input_data = load_input()
input_split = input_data.split("\n\n")

stacks = parse_stacks(input_split[0])
instructions = parse_instructions(input_split[1])

for instruction in instructions:
  stacks = instruction_move_9000(stacks, *instruction)

solution1 = get_top_containers(stacks)
print("answer1: {}".format(solution1))

# Part 2

def instruction_move_9001(stacks, amount, from_stack, to_stack):
  containers_from = []
  for _ in range(amount):
    containers_from.append(stacks[from_stack-1].pop(0))

  for _ in range(len(containers_from)):
    stacks[to_stack-1].insert(0, containers_from.pop())
  return stacks

stacks = parse_stacks(input_split[0]) # reset stack

for instruction in instructions:
  stacks = instruction_move_9001(stacks, *instruction)

solution2 = get_top_containers(stacks)
print("answer2: {}".format(solution2))
