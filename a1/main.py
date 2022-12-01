with open("input.txt", "r") as f:
	calories = [list(map(int, c.split("\n"))) for c in f.read().split("\n\n")]

def solve1(calories: [[int]]) -> int:
	return max(map(sum, calories))

def solve2(calories: [[int]]) -> int:
	return sum(sorted(list(map(sum, calories)))[-3:])

print(solve1(calories))
print(solve2(calories))
