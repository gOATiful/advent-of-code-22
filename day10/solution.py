input_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

input_data2 = """noop
addx 3
addx -5"""

def load_input(input_file_path = "day10/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

input_data = load_input()
# input_data = input_data2

CRT_WIDTH = 40

class CPU():
    def __init__(self, instruction_observer: list) -> None:
       self.cycle = 0
       self.register = 1
       self.instruction_observer = instruction_observer
       self.observed_values = []
       self.display = []

    def do_instruction(self, inst:str):
        self.increment_cycle()
        if "addx" in inst:
            instruction_split = inst.split(" ")
            self.increment_cycle()
            self.register += int(instruction_split[1])

    def increment_cycle(self):
        self.drawCRT()
        self.cycle += 1
        if self.cycle in self.instruction_observer:
            self.observed_values.append(self.register)

    def drawCRT(self):
        crt_draw_pixel = self.cycle % CRT_WIDTH
        draw_frame = [crt_draw_pixel-1, crt_draw_pixel, crt_draw_pixel+1]
        if self.register in draw_frame:
            self.display.append("#")
        else:
            self.display.append(".")

    def print_display(self):
        for i in range(len(self.display)):
            if i % CRT_WIDTH == 0:
                print()
            print(self.display[i], end="")
        

    def get_signal_strength(self):
        oberved_cnt = len(self.observed_values)
        return [self.observed_values[i] * self.instruction_observer[i] for i in range(oberved_cnt)]

cpu = CPU([20, 60, 100, 140, 180, 220])

for command in input_data.splitlines():
    cpu.do_instruction(command)

signal_strength = cpu.get_signal_strength()
print("Answer1:{}".format(sum(signal_strength)))
print("Answer2:")
cpu.print_display()
print()