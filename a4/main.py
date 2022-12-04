with open("input.txt", "r") as f:
	assignments = [line.strip().split(",") for line in f.readlines()]
	assignments = [(pair[0].split("-"), pair[1].split("-")) for pair in assignments]
	assignments = [(tuple(map(int, pair[0])), tuple(map(int, pair[1]))) for pair in assignments]

def contains(a, b):
	return a[0] <= b[0] and a[1] >= b[1]

def overlap(a, b):
	return contains(a, b) or (a[0] <= b[1] and a[1] >= b[1])

def solve1(assignments):
	return len(list(filter(lambda x: contains(x[0], x[1]) or contains(x[1], x[0]), assignments)))

def solve2(assignments):
	return len(list(filter(lambda x: overlap(x[0], x[1]) or overlap(x[1], x[0]), assignments)))

print(solve1(assignments))
print(solve2(assignments))
