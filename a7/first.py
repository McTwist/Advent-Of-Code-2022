with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]
	tree = {}
	stack = []
	curr = tree
	for line in lines:
		a = line.split(" ")
		if a[0] == "$":
			if a[1] == "cd":
				if a[2] == "/":
					stack = []
					curr = tree
				elif a[2] == "..":
					stack.pop()
					curr = tree
					for f in stack:
						curr = curr[f]
				else:
					stack.append(a[2])
					if a[2] not in curr:
						curr[a[2]] = {}
					curr = curr[a[2]]
			elif a[1] == "ls":
				pass
		elif a[0] == "dir":
			if a[1] not in curr:
				curr[a[1]] = {}
		else:
			if a[1] not in curr:
				curr[a[1]] = int(a[0])

def calc_size(tree: dict) -> int:
	tree["."] = 0
	for f, s in tree.items():
		if f.startswith("."):
			continue
		if isinstance(s, int):
			tree["."] += s
		else:
			tree["."] += calc_size(s)
	return tree["."]

def calc_smol_size(tree: dict) -> int:
	total = 0
	for f, s in tree.items():
		if f.startswith("."):
			continue
		if isinstance(s, int):
			continue
		else:
			total += calc_smol_size(s)
	if tree["."] < 100000:
		total += tree["."]
	return total

def list_dirs(tree: dict) -> list:
	l = [tree]
	for f, s in tree.items():
		if f.startswith("."):
			continue
		if not isinstance(s, int):
			l += list_dirs(s)
	return l

def solve1(tree):
	return calc_smol_size(tree)

def solve2(tree):
	total_disk = 70000000
	required_disk = 30000000
	current_used = tree["."]
	to_be_removed = required_disk - (total_disk - current_used)
	return min([d for d in list_dirs(tree) if d["."] > to_be_removed], key=lambda d: d["."])["."]

calc_size(tree)

print(solve1(tree))
print(solve2(tree))
