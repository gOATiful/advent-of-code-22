
input_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

class Directory():
    def __init__(self, name, parent):
      self.name = name
      self.parent = parent
      self.subtree = []

    def get_size(self):
      size = 0
      for f in self.subtree:
        if type(f) is Directory:
          size += f.get_size()
        else:
          size += f.size
      return size

    def get_dir(self, name):
      for f in self.subtree:
        if f.name == name:
          return f
      return None

    def contains(self, name):
      def condition(item):
        return item.name == name
      return len(list(filter(condition, self.subtree))) > 0

    def ls(self):
      print_str = "- {} (dir)\n".format(self.name)
      for branch in self.subtree:
        if type(branch) is Directory:
          print_str += "  " + branch.ls().replace("\n", "\n  ")
        else:
          print_str += "  - {} (file, size={})\n".format(branch.name, branch.size)
      return print_str

class File():
  def __init__(self, name, size):
    self.name = name
    self.size = size

def create_file_tree(input:str):
  root = Directory("/", None)
  current_dir = root
  for line in input.splitlines()[1:]: # skip entering into /
    if line.startswith("$ cd "): # change dir command
      dirname = line.removeprefix("$ cd ")
      if dirname == "..":
        current_dir = current_dir.parent
      elif dirname == "/":
        current_dir = root
      elif current_dir.contains(dirname):
        current_dir = current_dir.get_dir(dirname)
    elif line.startswith("$ ls"):
      pass
    else:
      line_split = line.split(" ")
      name = line_split[1]
      if line_split[0] == "dir":
        current_dir.subtree.append(Directory(name, current_dir))
      else: # file
        size = int(line_split[0])
        current_dir.subtree.append(File(name, size))
  return root
      

def load_input(input_file_path = "day7/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

def find_dirs_of_at_most(tree, size):
  filter_list = []
  if type(tree) is Directory:
    dir_size = tree.get_size()
    if dir_size < size:
      filter_list.append(tree)
    for subtree in tree.subtree:
      filter_list.extend(find_dirs_of_at_most(subtree, size))
  return filter_list
  
input_data = load_input()

file_tree = create_file_tree(input_data)

find_dirs_with_size = find_dirs_of_at_most(file_tree, 100000)

print(sum(x.get_size() for x in find_dirs_with_size))

# Part 2

total_space_on_device = 70000000
required_update_size = 30000000
space_used = file_tree.get_size()
space_free = total_space_on_device - space_used
space_to_free = required_update_size - space_free

def find_dirs_of_at_least(tree, size):
  filter_list = []
  if type(tree) is Directory:
    dir_size = tree.get_size()
    if dir_size > size:
      filter_list.append(tree)
    for subtree in tree.subtree:
      filter_list.extend(find_dirs_of_at_least(subtree, size))
  return filter_list
      
candidates = find_dirs_of_at_least(file_tree, space_to_free)
# find smallest
result2 = min(candidates, key=lambda x: x.get_size())
print(result2.get_size())