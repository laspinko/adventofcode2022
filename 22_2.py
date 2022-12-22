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

size = int(input('Cube size:'))
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arrows = ['>','V','<','^']

def rot_right(x, y):
	return size-1-y, x
def map_str(m):
	return '\n'.join([''.join(i) for i in m])
class CubeFace:
	def __init__(self, id):
		self.id = id
		self.map = [[]]
		self.neigh = {}
		self.x = 0
		self.y = 0
	def get_starting(self):
		for y in range(size):
			for x in range(size):
				if self.map[y][x] == '.':
					return x, y
	def set_coord(self, x, y):
		self.x = x
		self.y = y
	def add_cell(self, c):
		if len(self.map[-1]) < size:
			self.map[-1].append(c)
		else:
			self.map.append([c])
	def set_neigh(self,d,neigh, rot):
		self.neigh[d] = (neigh,rot)
	def get_neigh(self,d):
		if d not in self.neigh:
			n1, r1 = self.get_neigh((d+1)%4)
			n2, r2 = n1.get_neigh((d+r1)%4)
			self.neigh[d] = (n2, (r1+r2+1)%4)
		return self.neigh[d]
	def get_pos(self, _x, _y, d):
		x = _x + dir[d][0]
		y = _y + dir[d][1]
		if x >= 0 and x < size and y >= 0 and y < size:
			return self, x, y, d
		x %= size
		y %= size
		for _ in range((self.neigh[d][1])%4):
			x, y = rot_right(x,y)
		return self.neigh[d][0], x, y, (d+self.neigh[d][1])%4
	def move(self, _x, _y, d, t=0):
		f, x, y, _d = self.get_pos(_x, _y, d)
		if f.map[y][x] != '#':
			self.map[_y][_x] = arrows[d]#chr(ord('a')+t%26)#
			return f, x, y, _d, t+1
		return self, _x, _y, d, t
	def __repr__(self):
		return map_str(self.map)

cube = [CubeFace(i) for i in range(6)]

curr_face = -1
faceid = dict()
y = 0
map = []
while True:
	inp = input()
	if inp == '':
		break
	map.append([i for i in inp])
	for x in range(len(inp)):
		if inp[x] != ' ':
			if x % size == 0 and y % size == 0 and inp[x] != ' ':
				curr_face += 1
				if y//size not in faceid:
					faceid[y//size] = dict()
				faceid[y//size][x//size] = curr_face
				cube[curr_face].set_coord(x, y)
			cube[faceid[y//size][x//size]].add_cell(inp[x])
	y += 1
for _y in faceid:
	for _x in faceid[_y]:
		if _y in faceid and _x in faceid[_y]:
			for d in range(4):
				x = (_x + dir[d][0])
				y = (_y + dir[d][1])
				if y in faceid and x in faceid[y]:
					cube[faceid[_y][_x]].set_neigh(d, cube[faceid[y][x]], 0)


path = input()

print(faceid)
for c in range(6):
	print(f'{c}:')
	for d in range(4):
		n, r = cube[c].get_neigh(d)
		print(f'{n.id} at rotation {r}', flush=True)

curr_dir = 0
curr_len = 0
steps = []
for c in path:
	if ord(c) in range(ord('0'), ord('9')+1):
		curr_len *= 10
		curr_len += ord(c) - ord('0')
	else:
		steps.append((curr_dir, curr_len))
		curr_dir = 1 if c == 'R' else -1
		curr_len = 0
steps.append((curr_dir, curr_len))

# Simulation

f = cube[0]
x, y = f.get_starting()

t=0
d=0
for _d,l in steps:
	d = (d+_d)%4
	for _ in range(l):
		f, x, y, d, t = f.move(x, y, d, t)
		
for c in cube:
	for _x in range(size):
		for _y in range(size):
			map[_y+c.y][_x+c.x]=c.map[_y][_x]
print(map_str(map))
print((y+f.y+1)*1000 + (x+f.x+1)*4 + d)