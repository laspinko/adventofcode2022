rocks = [
	[['#','#','#','#']],
	
	[
	['.','#','.'],
	['#','#','#'],
	['.','#','.']],
	
	[
	['#','#','#'],
	['.','.','#'],
	['.','.','#']],
	
	[
	['#'],
	['#'],
	['#'],
	['#']],
	
	[
	['#','#'],
	['#','#']]
]


jet = input()
jdir = {'<': -1, '>': 1} #mirrored

mw = 7

map = [['#' for _ in range(mw)]]

def expand_map(y):
	global map
	map += [['.' for _ in range(mw)] for _ in range(y - len(map))]
def check_placement(r, x, y):
	w = len(rocks[r][0])
	h = len(rocks[r])
	if x < 0 or x + w > mw:
		return False
	for _x in range(w):
		for _y in range(h):
			if rocks[r][_y][_x] == '#' and map[y+_y][x+_x] == '#':
				return False
	return True
def place_rocks(r, x, y):
	global map
	w = len(rocks[r][0])
	h = len(rocks[r])
	for _x in range(w):
		for _y in range(h):
			if rocks[r][_y][_x] == '#':
				map[y+_y][x+_x] = '#'
def str_map():
	return '\n'.join([''.join(row) for row in map[::-1]])
def reduce_map():
	stopped = [False for _ in range(mw)]
	for y in range(len(map)-1, -1, -1):
		for x in range(mw):
			if map[y][x] == '#':
				stopped[x] = True
			elif not stopped[x]:
				for _x in range(x, mw):
					if map[y][_x] == '#':
						break
					stopped[_x] = False
				for _x in range(x, -1, -1):
					if map[y][_x] == '#':
						break
					stopped[_x] = False
		#print(''.join(['o' if s else ' ' for s in stopped]))
		#print(''.join(map[y]))
		if all(stopped):
			return y, map[y:]

r = 0
js = 0
mh = 0
cnt = 0

seen = dict() # (map, r, js) -> index of heights

heights = []
acc_red = 0

if int(input('Choose part:')) == 1:
	max_steps = 2022
else:
	max_steps = 1000000000000

while cnt < 2022:
	x = 2
	y = mh + 4
	expand_map(y+len(rocks[r]))
	while True:
		if check_placement(r, x + jdir[jet[js]], y):
			x += jdir[jet[js]]
		js = (js + 1) % len(jet)
		if check_placement(r, x, y-1):
			y -= 1
		else:
			break
	place_rocks(r, x, y)
	mh = max(mh, y + len(rocks[r]) - 1)
	
	r = (r + 1) % len(rocks)
	cnt += 1
	
	
	
	red, map = reduce_map()
	#print(cnt)
	#print(str_map(), '\n')
	acc_red += red
	mh -= red
	heights.append(mh + acc_red)
	
	
	key = (str_map(), r, js)
	if key in seen:
		print('loop found at',cnt)
		rem = max_steps - cnt
		dist = cnt - 1 - seen[key]
		ans = heights[-1]
		ans += (rem // dist) * (heights[-1] - heights[seen[key]])
		ans += heights[seen[key] + rem % dist] - heights[seen[key]]
		print(ans)
		break;
		pass
	else:
		seen[key] = cnt-1
	
if cnt == max_steps:
	print(heights[-1])