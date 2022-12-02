with open("input.txt", "r") as f:
	strategy = [tuple(map(
		lambda a: ord(a) - ord('A') if a in 'ABC' else ord(a) - ord('X'),
		line.strip().split())) for line in f.readlines()]

def calc_score(a, b):
	match a - b:
		case 1|-2: return 0
		case 0: return 3
		case -1|2: return 6

def solve1(strategy):
	score = 0
	for you, me in strategy:
		score += me + 1 + calc_score(you, me)
	return score

def solve2(strategy):
	score = 0
	for you, me in strategy:
		score += (((you + 3) + (me - 1)) % 3) + 1 + (me * 3)
	return score

print(solve1(strategy))
print(solve2(strategy))
