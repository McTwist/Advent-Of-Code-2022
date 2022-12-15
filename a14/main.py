with open('input.txt') as f:
	lines = [line.strip().split(" -> ") for line in f.readlines()]
	lines = [[tuple(map(int, l.split(","))) for l in line] for line in lines]

def prepare_stones(lines):
	stones = set()
	for line in lines:
		for i in range(len(line)-1):
			x1, y1 = line[i]
			x2, y2 = line[i+1]
			if x1 == x2:
				for y in range(min(y1, y2), max(y1, y2)+1):
					stones.add((x1, y))
			elif y1 == y2:
				for x in range(min(x1, x2), max(x1, x2)+1):
					stones.add((x, y1))
	return stones

def collide(stones, sand, x, y):
	return (x, y) in stones or (x, y) in sand

def fall(stones, sand, x, y):
	if not collide(stones, sand, x, y+1):
		return x, y+1
	if not collide(stones, sand, x-1, y+1):
		return x-1, y+1
	if not collide(stones, sand, x+1, y+1):
		return x+1, y+1
	return None

def solve1(lines):
	void = max([y for line in lines for _, y in line])
	stones = prepare_stones(lines)
	sand = set()
	while True:
		x, y = 500, 0
		while pos := fall(stones, sand, x, y):
			x, y = pos
			if y == void:
				return len(sand)
		sand.add((x, y))

def solve2(lines):
	void = max([y for line in lines for _, y in line])
	stones = prepare_stones(lines)
	sand = set()
	while True:
		x, y = 500, 0
		while pos := fall(stones, sand, x, y):
			x, y = pos
			if y == void+1:
				break
		sand.add((x, y))
		if (x, y) == (500, 0):
			return len(sand)

print(solve1(lines))
print(solve2(lines))

