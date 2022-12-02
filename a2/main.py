with open("input.txt", "r") as f:
	strategy = [tuple(map(
		lambda a: ord(a) - ord('A') if a in 'ABC' else ord(a) - ord('X'),
		line.strip().split())) for line in f.readlines()]

def solve1(strategy):
	score = 0
	for you, me in strategy:
		score += me + 1 + ((2 - (((you - me) + 4) % 3)) * 3)
	return score

def solve2(strategy):
	score = 0
	for you, me in strategy:
		score += (((you + 3) + (me - 1)) % 3) + 1 + (me * 3)
	return score

print(solve1(strategy))
print(solve2(strategy))
