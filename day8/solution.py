import copy
input_data = """30373
25512
65332
33549
35390"""


def load_input(input_file_path = "day8/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

# input_data = load_input()

def parse_forrest(input_data:str):
    forrest = []
    for line in input_data.splitlines():
        row = [int(x) for x in line]
        forrest.append(row)
    return forrest


def view_left(forrest: list[list]):
    forrest = copy.deepcopy(forrest) # ensure new list
    for row in forrest:
        yield row

def view_right(forrest: list[list]):
    forrest = copy.deepcopy(forrest) # ensure new list
    forrest = forrest.copy()
    for row in forrest:
        row.reverse()
        yield row

def view_top(forrest:list[list]):
    forrest = copy.deepcopy(forrest) # ensure new list
    forrest_view = [[] for _ in forrest[0]]
    for y in range(len(forrest)):
        for x in range(len(forrest)):
            forrest_view[x].append(forrest[y][x])
    for row in forrest_view:
        yield row

def view_bottom(forrest:list[list]):
    forrest = copy.deepcopy(forrest) # ensure new list
    row_len = len(forrest[0])
    forrest_view = [[] for _ in range(row_len)]
    for y in range(len(forrest)):
        for x in range(row_len):
            forrest_view[x].append(forrest[y][x])
    for row in forrest_view:
        row.reverse()
        yield row

def cnt_visible_trees(forrest):
    print("left")

    for row in view_left(forrest):
        



forrest = parse_forrest(input_data)
cnt_visible_trees(forrest)