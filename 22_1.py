'''
        ...#    
        .#..    
        #...    
        ....    
...#.......#    
........#...    
..#....#....    
..........#.    
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
'''

'''
final arrangement:

.12
.3.
45.
6..


'''
face_transitions = 
	{
		1:{}
	}

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arrows = ['>','V','<','^']
map = []

top = []
bottom = []
left = []
right = []
w = 0
h = 0
while True:
	inp = input()
	if inp == '':
		break
	map.append([i for i in inp])
	h += 1
	for _ in range(len(inp)-len(top)):
		top.append(-1)
		bottom.append(-1)
		w += 1
	sp = 0
	for i in range(len(inp)):
		if inp[i] != ' ':
			bottom[i] = len(map)-1
			if top[i] == -1:
				top[i] = len(map)-1
	right.append(len(inp)-1)
	left.append(len(inp)-len(inp.strip()))
path = input()

curr_dir = 0
curr_len = 0
steps = []
for c in path:
	if ord(c) in range(ord('0'), ord('9')+1):
		curr_len *= 10
		curr_len += ord(c) - ord('0')
	else:
		steps.append((curr_dir, curr_len))
		curr_dir = (curr_dir + 4 + (1 if c == 'R' else -1)) % 4
		curr_len = 0
steps.append((curr_dir, curr_len))

def move(_x, _y, d):
	x = _x+d[0]
	y = _y+d[1]
	if d[0] != 0:
		if x > right[y]:
			x = left[y]
		if x < left[y]:
			x = right[y]
	if d[1] != 0:
		if y > bottom[x]:
			y = top[x]
		if y < top[x]:
			y = bottom[x]
	if map[y][x] not in ['#', ' ']:
		return (x, y)
	else:
		return (_x, _y)

x = map[0].index('.')
y = 0
for d,l in steps:
	print(d, l, x, y, flush=True)
	for _ in range(l):
		x, y = move(x, y, dir[d])
		map[y][x] = arrows[d]

print('\n'.join([''.join(i) for i in map]))

print((y+1)*1000+(x+1)*4+steps[-1][0])