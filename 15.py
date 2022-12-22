import re
class Sensor:
	def __init__(self, x, y, bx, by):
		self.x = x
		self.y = y
		self.bx = bx
		self.by = by
		self.r = abs(x - bx) + abs(y - by)
	def inside(self, x, y):
		return abs(x - self.x) + abs(y - self.y) <= self.r
	def get_row(self, y):
		return self.x - (self.r - abs(self.y - y)), self.x + (self.r - abs(self.y - y))

s = []
b = set()

yrow = 2000000

while True:
	inp = input()
	if(inp == '.'):
		break;
	inp = re.findall(r'\d+', inp)
	inp = [int(i) for i in inp]
	s.append(Sensor(inp[0], inp[1], inp[2], inp[3]))
	if inp[3] == yrow:
		b.add(inp[2])

def part1():
	ans = 0
	p = []
	for i in s:
		sx, fx = i.get_row(yrow)
		if sx <= fx:
			p.append((sx, 0))
			p.append((fx+1,1))
			
	p.sort()

	cnt = 0
	for i in range(len(p) - 1):
		(x, t) = p[i]
		if t == 0:
			cnt += 1
		else:
			cnt -= 1
		if cnt > 0:
			ans += p[i+1][0] - x
	return ans - len(b)
def part2(mx, my):
	for y in range(0, my+1):
		p = []
		for i in s:
			sx, fx = i.get_row(y)
			if sx <= fx:
				sx = max(sx, 0)
				fx = min(fx, mx)
				p.append((sx, 0))
				p.append((fx+1,1))
		p.sort()
		cnt = 0
		for i in range(len(p) - 1):
			(x, t) = p[i]
			if t == 0:
				cnt += 1
			else:
				cnt -= 1
			if x != p[i+1][0] and cnt == 0:
				return x * 4000000 + y
print(part2(4000000,4000000))