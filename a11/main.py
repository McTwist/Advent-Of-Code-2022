import re
from itertools import cycle
import copy

with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

class Monkey:
	def __init__(self, operation, test, iftrue, iffalse):
		self.__items = []
		self.__operation = operation
		self.__test = test
		self.__iftrue = iftrue
		self.__iffalse = iffalse
		self.__inspected = 0
	def additem(self, item):
		self.__items.append(item)
	def items(self):
		return self.__items
	def divisible(self):
		return self.__test
	def shenanigan(self, worried=False):
		while self.__items:
			item = self.__items.pop(0)
			worry = self.inspect(item)
			if not worried:
				worry //= 3
			yield (self.test(worry), worry)
	def inspected(self):
		return self.__inspected
	def inspect(self, item):
		self.__inspected += 1
		a = item if self.__operation[0] == "old" else int(self.__operation[0])
		b = item if self.__operation[2] == "old" else int(self.__operation[2])
		if self.__operation[1] == "*":
			c = a * b
		elif self.__operation[1] == "+":
			c = a + b
		return c
	def test(self, item):
		return self.__iftrue if item % self.__test == 0 else self.__iffalse

def populate(lines):
	rmonkey = re.compile(r'Monkey (\d+)')
	rstarting = re.compile(r'Starting items: (.*)')
	roperation = re.compile(r'Operation: new = ([\w\d]*) ([*+]) ([\w\d]*)')
	rtest = re.compile(r'Test: divisible by (\d+)')
	riftrue = re.compile(r'If true: throw to monkey (\d+)')
	riffalse = re.compile(r'If false: throw to monkey (\d+)')

	monkeys = []
	for i in range(0, len(lines), 7):
		# Note: Ignores the #monkey
		_ = int(rmonkey.match(lines[i])[1])
		starting = map(int, rstarting.match(lines[i+1])[1].split(", "))
		operation = roperation.match(lines[i+2]).groups()
		test = int(rtest.match(lines[i+3])[1])
		iftrue = int(riftrue.match(lines[i+4])[1])
		iffalse = int(riffalse.match(lines[i+5])[1])
		monkey = Monkey(operation, test, iftrue, iffalse)
		for item in starting:
			monkey.additem(item)
		monkeys.append(monkey)
	return monkeys

def solve1(monkeys):
	for i in range(20):
		for monkey in monkeys:
			for m, w in monkey.shenanigan():
				monkeys[m].additem(w)
	sort = sorted(monkeys, reverse=True, key=lambda m: m.inspected())
	return sort[0].inspected() * sort[1].inspected()

def solve2(monkeys):
	div = 1
	# Note: All divisibles are primes, so no need to lcm
	for monkey in monkeys:
		div *= monkey.divisible()
	for i in range(10000):
		for monkey in monkeys:
			for m, w in monkey.shenanigan(True):
				monkeys[m].additem(w % div)
	sort = sorted(monkeys, reverse=True, key=lambda m: m.inspected())
	return sort[0].inspected() * sort[1].inspected()

monkeys = populate(lines)

print(solve1(copy.deepcopy(monkeys)))
print(solve2(copy.deepcopy(monkeys)))
