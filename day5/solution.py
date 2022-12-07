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

def parse_stack(input: str):
    lines = input.splitlines()
    stack_cnt = (len(lines[-1]) +1) / chars_per_container

    for line in input.splitlines()[:-1]:
        for i in range(stack_cnt):
            container = line[chars_per_container * i + 1]
        print(line)

# input_data = load_input()
input_split = input_data.split("\n\n")

stack = parse_stack(input_split[0])
instructions = input_split[1]

print(stack)