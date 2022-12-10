with open("input.txt", "r") as f:
	instructions = [tuple(line.strip().split(" ")) for line in f.readlines()]

class ClockCircuit:
	def __init__(self):
		self.__cycles = [1]
		self.__screen = [""]*6
	def cycle(self, instruction):
		self.instruct(instruction)
	def instruct(self, instruction):
		match instruction[0]:
			case "noop":
				self.draw()
				self.__cycles.append(self.__cycles[-1])
			case "addx":
				self.draw()
				self.__cycles.append(self.__cycles[-1])
				self.draw()
				self.__cycles.append(self.__cycles[-1] + int(instruction[1]))
	def draw(self):
		i = len(self.__cycles)-1
		sprite = self.__cycles[-1]
		self.__screen[i // 40] += "#" if sprite-1 <= (i % 40) <= sprite+1 else "."
	def strength(self):
		return sum(self.__cycles[i] * (i+1) for i in range(19, len(self.__cycles), 40))
	def screen(self):
		return "\n".join(self.__screen)

def solve1(instructions):
	circuit = ClockCircuit()
	for instruction in instructions:
		circuit.cycle(instruction)
	return circuit.strength()

def solve2(instructions):
	circuit = ClockCircuit()
	for instruction in instructions:
		circuit.cycle(instruction)
	return circuit.screen()

print(solve1(instructions))
print(solve2(instructions))
