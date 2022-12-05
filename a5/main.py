import re

rmove = re.compile(r"move (\d+) from (\d+) to (\d+)")
with open("input.txt", "r") as f:
	lines = f.readlines()
	moves = None
	placement = []
	for line in lines:
		if moves is None:
			if line == "\n":
				moves = []
			else:
				placement.append(line)
		else:
			m = rmove.match(line)
			moves.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))
	place = [""] * (len(placement[0]) // 4)
	for p in placement:
		for i in range(len(p) // 4):
			pp = p[i * 4 + 1]
			place[i] = pp + place[i]
	towers = [c[1:].strip() for c in place]

def solve1(towers, moves):
	towers = towers.copy()
	for a, f, t in moves:
		s = towers[f-1][-a:][::-1]
		towers[f-1] = towers[f-1][:-a]
		towers[t-1] += s
	return "".join([c[-1] for c in towers])

def solve2(towers, moves):
	towers = towers.copy()
	for a, f, t in moves:
		s = towers[f-1][-a:]
		towers[f-1] = towers[f-1][:-a]
		towers[t-1] += s
	return "".join([c[-1] for c in towers])

print(solve1(towers, moves))
print(solve2(towers, moves))
