x = 1
c = 1

ans = 0

screen = [['.' for i in range(40)] for j in range(6)]

hx = 0
hy = 0

def incrC():
	global c, ans, hx, hy
	
	hx += 1
	if hx >= 40:
		hx = 0
		hy = (hy+1)%6
	
	if abs(hx - x) <= 1:
		screen[hy][hx] = '#'
	
	c += 1
	if c % 40 == 20:
		print('round ', c, '=', x)
		ans += x * c
while True:
	inp = input()
	if(inp == '.'):
		break;
	inp = inp.split()
	if inp[0] == 'noop':
		incrC()
	else:
		incrC()
		x += int(inp[1])
		incrC()
print(ans)
for row in screen:
	str = ''
	for col in row:
		str += col
	print(str)