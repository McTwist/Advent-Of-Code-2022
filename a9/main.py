with open("input.txt", "r") as f:
	moves = [tuple(line.strip().split(" ")) for line in f.readlines()]
	moves = [(a, int(b)) for a, b in moves]

def normalize(d):
	return d / abs(d)

class Knot:
	def __init__(self):
		self.x = 0
		self.y = 0
	def pos(self):
		return self.y, self.x

class Rope:
	def __init__(self, knots):
		self.__rope = [Knot() for _ in range(knots)]
		self.__visited = {}
	def visited(self):
		return len(self.__visited)
	def move(self, direction, steps):
		match direction:
			case "L":
				for _ in range(steps):
					self.__rope[0].x -= 1
					self._update()
			case "R":
				for _ in range(steps):
					self.__rope[0].x += 1
					self._update()
			case "U":
				for _ in range(steps):
					self.__rope[0].y += 1
					self._update()
			case "D":
				for _ in range(steps):
					self.__rope[0].y -= 1
					self._update()
	def _update(self):
		for i in range(1, len(self.__rope)):
			self._follow(i, i-1)
		self.__visited[self.__rope[-1].pos()] = True
	def _follow(self, a, b):
		a = self.__rope[a]
		b = self.__rope[b]
		if a.x > b.x+1:
			a.x -= 1
			if a.y != b.y:
				a.y += normalize(b.y - a.y)
		elif a.x < b.x-1:
			a.x += 1
			if a.y != b.y:
				a.y += normalize(b.y - a.y)
		elif a.y < b.y-1:
			a.y += 1
			if a.x != b.x:
				a.x += normalize(b.x - a.x)
		elif a.y > b.y+1:
			a.y -= 1
			if a.x != b.x:
				a.x += normalize(b.x - a.x)

def solve1(moves):
	rope = Rope(2)
	for move in moves:
		rope.move(*move)
	return rope.visited()

def solve2(moves):
	rope = Rope(10)
	for move in moves:
		rope.move(*move)
	return rope.visited()

print(solve1(moves))
print(solve2(moves))
