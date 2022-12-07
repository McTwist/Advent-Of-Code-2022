class File:
	def __init__(self, s):
		self.__size = s
	def size(self):
		return self.__size

class Dir:
	def __init__(self):
		self.__size = None
		self.__content = {}
	def __setitem__(self, key, item):
		self.__content[key] = item
	def __getitem__(self, key):
		return self.__content[key]
	def __contains__(self, key):
		return key in self.__content
	def __iter__(self):
		return iter(self.__content.values())
	def __str__(self):
		return str(self.__content)
	def size(self):
		if self.__size is None:
			self.__size = sum(d.size() for d in self.__content.values())
		return self.__size
	def add_dir(self, d):
		if d not in self:
			self[d] = Dir()
			self.__size = None
		return self[d]
	def add_file(self, f, s):
		if f not in self:
			self[f] = File(s)
			self.__size = None
		return self[f]
	def to_list(self):
		return list(self.__content.values()) + [dd for d in self if isinstance(d, Dir) for dd in d.to_list()]

with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]
	tree = Dir()
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
						curr.add_dir(a[2])
					curr = curr[a[2]]
			elif a[1] == "ls":
				pass
		elif a[0] == "dir":
			curr.add_dir(a[1])
		else:
			curr.add_file(a[1], int(a[0]))

def solve1(tree):
	total = 0
	for a in tree:
		if isinstance(a, Dir):
			total += solve1(a)
	if tree.size() < 100000:
		total += tree.size()
	return total

def solve2(tree):
	total_disk = 70000000
	required_disk = 30000000
	current_used = tree.size()
	to_be_removed = required_disk - (total_disk - current_used)
	return min([d.size() for d in tree.to_list() if isinstance(d, Dir) and d.size() > to_be_removed])

print(solve1(tree))
print(solve2(tree))
