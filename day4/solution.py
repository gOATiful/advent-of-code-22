input_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def load_input(input_file_path = "day4/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

input_data = load_input()

def create_section(sections):
  section_split = sections.split("-")
  start = int(section_split[0])
  end = int(section_split[1])
  return [x for x in range(start, end+1)]

def create_pair(row: str):
  row_split = row.split(",")
  first = row_split[0]
  first_section = create_section(first)
  second = row_split[1]
  second_section = create_section(second)
  return (first_section, second_section)

fully_contained = 0

overlap_at_all = 0

for pair_row in input_data.splitlines():
  pair = create_pair(pair_row)
  l_first = len(pair[0])
  l_second = len(pair[1])
  l_union = len(set(pair[0]) | set(pair[1]))
  # if the length of either matches the union => fully contained
  if l_first == l_union or l_second == l_union:
    fully_contained += 1
  # if the lenth of the unioin is not length of first + second => overlap
  if l_union != l_first+l_second:
    overlap_at_all +=1

print("Answer1: {}".format(fully_contained))
print("Answer2: {}".format(overlap_at_all))


