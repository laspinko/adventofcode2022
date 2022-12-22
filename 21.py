monkeys = dict()

class Monkey:
	def __init__(self, op, a=None, b = None):
		self.op = op
		self.a = a
		self.b = b
	def calc(self):
		match self.op:
			case 'const':
				return self.a
			case '*':
				return monkeys[self.a].calc()*monkeys[self.b].calc()
			case '+':
				return monkeys[self.a].calc()+monkeys[self.b].calc()
			case '-':
				return monkeys[self.a].calc()-monkeys[self.b].calc()
			case '/':
				return monkeys[self.a].calc()//monkeys[self.b].calc()
			case '=':
				v1 = v2 = None
				try:
					v1 = monkeys[self.a].clac()
				except:
					v2 = monkeys[self.b].calc()
				return monkeys[self.b].var_missing(v1) if v1 else monkeys[self.a].var_missing(v2)
			case 'var':
				raise ValueError('var found')
	def var_missing(self, val):
		if self.op == 'var':
			return val
		v1 = None
		v2 = None
		try:
			v1 = monkeys[self.a].calc()
		except ValueError:
			v2 = monkeys[self.b].calc()
		match self.op:
			case 'const':
				raise Exception
			case '*':
				return monkeys[self.b].var_missing(val // v1) if v1 else monkeys[self.a].var_missing(val // v2)
			case '+':
				return monkeys[self.b].var_missing(val - v1) if v1 else monkeys[self.a].var_missing(val - v2)
			case '-':
				return monkeys[self.b].var_missing(v1 - val) if v1 else monkeys[self.a].var_missing(val + v2)
			case '/':
				return monkeys[self.b].var_missing(v1 // val) if v1 else monkeys[self.a].var_missing(val * v2)
	def __repr__(self):
		if self.op == 'const':
			return str(self.a)
		elif self.op == 'var':
			return 'x'
		else:
			return f'({monkeys[self.a]}{self.op}{monkeys[self.b]})'
while True:
	inp = input()
	if inp == '.':
		break
	inp = inp.split()
	name = inp[0][:-1]
	if len(inp) == 2:
		monkeys[name] = Monkey('const', int(inp[1]))
	else:
		monkeys[name] = Monkey(inp[2], inp[1],inp[3])

if int(input('Choose part:')) == 2:
	monkeys['root'].op = '='
	monkeys['humn'] = Monkey('var')
print(monkeys['root'].calc())