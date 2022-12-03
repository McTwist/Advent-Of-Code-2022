with open("input.txt", "r") as f:
	rucksacks = [line.strip() for line in f.readlines()]

def calc_priority(a):
	a = ord(a)
	if ord('a') <= a <= ord('z'):
		return a - ord('a') + 1
	if ord('A') <= a <= ord('Z'):
		return a - ord('A') + 27

def intersect(a, b):
	found = []
	for item in a:
		if item in b:
			found.append(item)
	return found

def calc_similar(a, b):
	return calc_priority(intersect(a, b)[0])

def solve1(rucksacks):
	total = 0
	for rucksack in rucksacks:
		total += calc_similar(rucksack[len(rucksack)//2:], rucksack[:len(rucksack)//2])
	return total

def solve2(rucksacks):
	total = 0
	for i in range(len(rucksacks) // 3):
		first, second, third = tuple(rucksacks[i*3:i*3+3])
		total += calc_similar(intersect(first, second), third)
	return total

print(solve1(rucksacks))
print(solve2(rucksacks))
