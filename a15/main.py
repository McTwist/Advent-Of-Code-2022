import re

m = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
with open("input.txt", "r") as f:
	lines = [tuple(map(int, l)) for line in f.readlines() for l in m.findall(line.strip())]

def is_sample(lines):
	return lines[0][0] <= 20

def solve1(lines):
	y = 10 if is_sample(lines) else 2_000_000
	poss = []
	for sensorx, sensory, beaconx, beacony in lines:
		t = sum((abs(sensorx - beaconx), abs(sensory - beacony)))
		d = abs(y - sensory)
		if t < d:
			continue
		poss.append(sensorx - (t - d))
		poss.append(sensorx + (t - d))
	return max(poss) - min(poss)

def solve2(lines):
	for y in range(0, 21 if is_sample(lines) else 4_000_001):
		poss = []
		for sensorx, sensory, beaconx, beacony in lines:
			t = sum((abs(sensorx - beaconx), abs(sensory - beacony)))
			d = abs(y - sensory)
			if t < d:
				continue
			poss.append((sensorx - (t - d), sensorx + (t - d)))
		while len(poss) > 1:
			dl, dr = poss.pop(0)
			for al, ar in poss:
				if dl <= ar and dr >= al:
					poss.remove((al, ar))
					poss.append((min(dl, al), max(dr, ar)))
					break
			else:
				x = min(dr, poss[0][1])+1
				return x * 4_000_000 + y

print(solve1(lines))
print(solve2(lines))
