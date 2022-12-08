import copy
input_data = """30373
25512
65332
33549
35390"""


def load_input(input_file_path = "day8/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

input_data = load_input()

def parse_forrest(input_data:str):
    forrest = []
    for line in input_data.splitlines():
        row = [int(x) for x in line]
        forrest.append(row)
    return forrest

def trees_left_of(x, y, forrest):
    for i in range(x):
        yield forrest[y][x-i-1]

def trees_top_of(x, y, forrest):
    for i in range(y):
        yield forrest[y-i-1][x]

def trees_right_of(x, y, forrest):
    row_last_idx = len(forrest[0]) -1
    for i in range(x, row_last_idx):
        yield forrest[y][i+1]

def trees_bottom_of(x, y, forrest):
    col_last_idx = len(forrest[0]) -1
    for i in range(y, col_last_idx):
        yield forrest[i+1][x]


def is_tree_visible_from_direction(considered_tree_hight, trees_in_direction):
    for other_tree in trees_in_direction:
        if other_tree >= considered_tree_hight:
            return False
    return True


def is_tree_visible_any_direction(x, y, forrest):
    directions = [trees_left_of, trees_top_of, trees_right_of, trees_bottom_of]
    is_tree_visible = False
    considered_hight = forrest[y][x]
    for trees_in_direction in directions:
        trees_in_los = trees_in_direction(x, y, forrest)
        is_tree_visible |= is_tree_visible_from_direction(considered_hight, trees_in_los)
    return is_tree_visible


def cnt_inner_visible_trees(forrest):
    visible_trees = 0
    for y in range(1, len(forrest)-1):
        for x in range(1, len(forrest[0])-1):
            if is_tree_visible_any_direction(x, y, forrest):
                visible_trees += 1
    return visible_trees

def cnt_outer_visible_trees(forrest):
    return 2 * len(forrest[0]) + 2*(len(forrest) - 2)

forrest = parse_forrest(input_data)
visible_trees = cnt_outer_visible_trees(forrest)
visible_trees += cnt_inner_visible_trees(forrest)
print("Answer1: {}".format(visible_trees))

# Part 2

def view_distance_in_direction(considered_hight, trees_in_direction):
    view_distance = 0
    for other_tree_hight in trees_in_direction:
        view_distance += 1
        if considered_hight <= other_tree_hight:
            break
    return view_distance

def view_distance_in_any_direction(x, y, forrest):
    considered_hight = forrest[y][x]
    directions = [trees_left_of, trees_top_of, trees_right_of, trees_bottom_of]
    scienic_score = 1
    for tree_viewer in directions:
        trees_in_direction = tree_viewer(x,y,forrest)
        scienic_score *= view_distance_in_direction(considered_hight, trees_in_direction)
    return scienic_score


def find_max_scienic_score(forrest):
    max_score = 0
    for y in range(1, len(forrest)-1):
        for x in range(1, len(forrest[0])-1):
            score = view_distance_in_any_direction(x, y, forrest)
            if score > max_score:
                max_score = score
    return max_score

max_scenic_score = find_max_scienic_score(forrest)
print("Answer2: {}".format(max_scenic_score))