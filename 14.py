
w = 501
h = 0
floor = 0

map = [['.' for _ in range(w)] for _ in range(h)]

def expand(nw, nh):
	global w, h, map
	if nw > w:
		for row in map:
			row += ['.' for _ in range(nw - w)]
		w = nw
	if nh > h:
		for i in range(nh - h):
			map.append(['.' for _ in range(w)])
		h = nh
def expand_left():
	global w, map
	for row in map:
		row = ['.'] + row
	w += 1

while True:
	inp = input()
	if(inp == '.'):
		break;
	inp = inp.split(' -> ')
	inp = [[int(num) for num in i.split(',')] for i in inp]
	for i in inp:
		expand(i[0]+1, i[1]+1)
		floor = max(floor, i[1] + 2)
	for i in range(1, len(inp)):
		if inp[i-1][0] == inp[i][0]:
			for j in range(min(inp[i-1][1], inp[i][1]), max(inp[i-1][1], inp[i][1])+1):
				map[j][inp[i][0]] = '#'
		else:
			for j in range(min(inp[i-1][0], inp[i][0]), max(inp[i-1][0], inp[i][0])+1):
				map[inp[i][1]][j] = '#'

expand(w, floor)

def sand():
	global map
	x,y = 500,0
	if map[0][500] != '.':
		return False
	while True:
		if y == h-1:
			map[y][x] = 'o'
			return True
		elif map[y+1][x] == '.':
			y += 1
		elif x == 0:
			expand_left()
			y += 1
			x -= 1
		elif map[y+1][x-1] == '.':
			y += 1
			x -= 1
		elif x == w-1:
			expand(w+1, h)
			y += 1
			x += 1
		elif map[y+1][x+1] == '.':
			y += 1
			x += 1
		else:
			map[y][x] = 'o'
			return True
			

cnt = 0
while sand():
	cnt += 1



print('\n'.join([''.join(i) for i in map]))

print(cnt)