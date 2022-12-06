with open("input.txt", "r") as f:
	data = f.read()

def marker(data, distinct):
	for i in range(distinct-1, len(data)):
		if len(set(data[i-(distinct-1):i+1])) == distinct:
			return i+1

def solve1(data):
	return marker(data, 4)

def solve2(data):
	return marker(data, 14)

print(solve1(data))
print(solve2(data))
