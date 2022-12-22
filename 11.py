import math

monkeys = []

class Monkey:
	def __init__(self, has, op, t, tt, tf):
		self.has = has
		self.op = op
		self.test = t
		self.ttrue = tt
		self.tfalse = tf
		self.inspected = 0
		
lcm = 1
while True:
	name = input()
	if(name == '.'):
		break;
	starting = input().split()
	starting = [int(i.split(',')[0]) for i in starting[2:]]
	print(starting)
	operation = input().split()
	if operation[-2] == '+':
		if operation[-1] == 'old':
			operation = lambda x: 2*x
		else:
			operation = lambda x, y = int(operation[-1]): x + y
	else:
		if operation[-1] == 'old':
			operation = lambda x: x*x
		else:
			operation = lambda x, y = int(operation[-1]): x * y
	test = int(input().split()[-1])
	ttrue = int(input().split()[-1])
	tfalse = int(input().split()[-1])
	lcm = math.lcm(lcm, test)
	monkeys.append(Monkey(starting, operation, test, ttrue, tfalse))
	input()

print(lcm)

def take_turn(m):
	global monkeys
	for i in m.has:
		ni = m.op(i) % lcm# // 3 # return for part 1
		monkeys[m.ttrue if ni % m.test == 0 else m.tfalse].has.append(ni)
		m.inspected += 1
	m.has = []

for r in range(10000):
	for m in monkeys:
		take_turn(m)
	if r % 1000 == 0:
		print(r, ' rounds completed', flush=True)

insp = []
for m in monkeys:
	print(m.inspected)
	insp.append(m.inspected)
insp.sort()
print(insp[-1]*insp[-2])
