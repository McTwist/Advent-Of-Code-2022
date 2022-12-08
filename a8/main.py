with open("input.txt", "r") as f:
	trees = [list(map(int, list(line.strip()))) for line in f.readlines()]

def is_visible(trees, x, y):
	p = trees[y][x]
	return not (
		[True for i in range(x) if trees[y][i] >= p] and
		[True for i in range(x+1, len(trees[y])) if trees[y][i] >= p] and
		[True for i in range(y) if trees[i][x] >= p] and
		[True for i in range(y+1, len(trees)) if trees[i][x] >= p])

def score(trees, x, y):
	p = trees[y][x]
	t1, t2, t3, t4 = 0, 0, 0, 0
	for i in range(x-1, -1, -1):
		t1 += 1
		if trees[y][i] >= p:
			break
	for i in range(x+1, len(trees[y])):
		t2 += 1
		if trees[y][i] >= p:
			break
	for i in range(y-1, -1, -1):
		t3 += 1
		if trees[i][x] >= p:
			break
	for i in range(y+1, len(trees)):
		t4 += 1
		if trees[i][x] >= p:
			break
	return t1 * t2 * t3 * t4

def solve1(trees):
	visible = len(trees) * 2 + (len(trees[0]) - 2) * 2
	for y in range(1, len(trees) - 1):
		for x in range(1, len(trees[y]) - 1):
			if is_visible(trees, x, y):
				visible += 1
	return visible

def solve2(trees):
	return max(score(trees, x, y) for y in range(1, len(trees)-1) for x in range(1, len(trees[y])-1))

print(solve1(trees))
print(solve2(trees))
