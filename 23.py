dir = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0, 1), (-1,1), (-1,0)]
ord = [1, 5, 7, 3]
elves = []

y = 0
while True:
	inp = input()
	if inp == '':
		break
	for x in range(len(inp)):
		if inp[x] == '#':
			elves.append([x,y])
	y += 1

def get_range():
	return min([e[0] for e in elves]), max([e[0] for e in elves]), min([e[1] for e in elves]), max([e[1] for e in elves])
def print_elves():
	minx, maxx, miny, maxy = get_range()
	map = [['.' for _ in range(minx, maxx+1)] for _ in range(miny, maxy+1)]
	for x,y in elves:
		map[y-miny][x-minx] = '#'
	print('\n'.join([''.join(i) for i in map]))
def sym_round():
	global elves, ord
	curr = {(x, y) for x,y in elves}
	next = {}
	
	skipped = 0
	
	#proposing
	for i in range(len(elves)):
		x, y = elves[i]
		neigh = 0
		for dx, dy in dir:
			if (dx+x, dy+y) in curr:
				neigh += 1
		if neigh == 0:
			skipped += 1
			continue
		
		for o in ord:
			neigh = 0
			for k in range(-1,2):
				dx, dy = dir[(o+k)%8]
				if (dx+x, dy+y) in curr:
					neigh += 1
			if neigh == 0:
				prop = (x+dir[o][0], y+dir[o][1])
				if prop not in next:
					next[prop] = []
				next[prop].append(i)
				break
	if skipped == len(elves):
		return False
	#moving
	for (nx,ny), ids in next.items():
		if len(ids) == 1:
			elves[ids[0]] = [nx,ny]
	#change ord
	ord = ord[1:] + [ord[0]]
	return True
	#print(elves)
	#print_elves()

if int(input('Choose part:')) == 1:
	for t in range(10):
		sym_round()
	minx, maxx, miny, maxy = get_range()
	print((maxx-minx+1)*(maxy-miny+1) - len(elves))
else:
	cnt = 1
	while sym_round():
		cnt += 1
	print(cnt)