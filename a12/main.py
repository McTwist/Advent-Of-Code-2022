from queue import PriorityQueue

def to_height(a):
	match a:
		case 'S': a = 'a'
		case 'E': a = 'z'
	return ord(a) - ord('a')

def locate(heightmap, a):
	for y in range(len(heightmap)):
		for x in range(len(heightmap[y])):
			if heightmap[y][x] == a:
				return x, y

with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]
	start = locate(lines, 'S')
	end = locate(lines, 'E')
	heightmap = [list(map(to_height, line)) for line in lines]

def search(heightmap, starts, end):
	endx, endy = end
	queue = PriorityQueue()
	visited = set()
	for start in starts:
		visited.add(start)
		queue.put((0, start))
	def can_climb(c, x, y):
		if not 0 <= y < len(heightmap) or not 0 <= x < len(heightmap[y]):
			return False
		return heightmap[y][x] - c <= 1
	def climb(c, pos, prio):
		if pos not in visited and can_climb(c, *pos):
			visited.add(pos)
			queue.put((prio+1, pos))

	while not queue.empty():
		prio, (x, y) = queue.get()
		if x == endx and y == endy:
			break
		climb(heightmap[y][x], (x-1, y), prio)
		climb(heightmap[y][x], (x+1, y), prio)
		climb(heightmap[y][x], (x, y-1), prio)
		climb(heightmap[y][x], (x, y+1), prio)

	return prio

def solve1(heightmap, start, end):
	return search(heightmap, [start], end)

def solve2(heightmap, start, end):
	starts = [(x, y) for y in range(len(heightmap)) for x in range(len(heightmap[y])) if heightmap[y][x] == 0]
	return search(heightmap, starts, end)

print(solve1(heightmap, start, end))
print(solve2(heightmap, start, end))
