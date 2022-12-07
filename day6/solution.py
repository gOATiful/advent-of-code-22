input_data = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

def load_input(input_file_path = "day6/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

input_data = load_input()

def find_startcode(input_data, window_size):
    for i in range(0, len(input_data)-window_size):
        window = input_data[i:i+window_size]
        window_set = set(window)
        if len(window_set) == window_size:
            return i+window_size
    return -1

# Part 1
window_size_part1 = 4
part1_solution = find_startcode(input_data, window_size_part1)
print("Answer1: {}".format(part1_solution))


# Part 2
window_size_part2 = 14
part2_solution = find_startcode(input_data, window_size_part2)
print("Answer2: {}".format(part2_solution))