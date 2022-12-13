from functools import cmp_to_key
import json

with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]
	pairs = []
	for i in range(0, len(lines), 3):
		pairs.append((json.loads(lines[i]), json.loads(lines[i+1])))

def compare(l, r):
	if isinstance(l, int) and isinstance(r, int):
		if l < r:
			return 1
		elif l > r:
			return -1
		else:
			return 0
	elif isinstance(l, list) and isinstance(r, list):
		for i in range(len(l)):
			if i == len(r):
				return -1
			c = compare(l[i], r[i])
			if c != 0:
				return c
		return 1 if len(l) < len(r) else 0
	else:
		if isinstance(l, int):
			return compare([l], r)
		else:
			return compare(l, [r])

def solve1(pairs):
	return sum([i+1 for i in range(len(pairs)) if compare(*pairs[i]) >= 0])

def solve2(pairs):
	li = [a for l in pairs for a in l]
	first = [[2]]
	second = [[6]]
	li.append(first)
	li.append(second)
	li = sorted(li, key=cmp_to_key(compare), reverse=True)
	la = [i+1 for i in range(len(li)) if li[i] == first or li[i] == second]
	return la[0] * la[1]

print(solve1(pairs))
print(solve2(pairs))
