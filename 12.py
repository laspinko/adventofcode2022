import queue

map = []

s = ()
e = ()

while True:
	inp = input()
	if(inp == '.'):
		break;
	inp = [i for i in inp]
	for i in range(len(inp)):
		if inp[i] == 'S':
			s = (len(map), i)
			inp[i] = 'a'
		if inp[i] == 'E':
			e = (len(map), i)
			inp[i] = 'z'
	map.append(inp)


w = len(map[0])
h = len(map)

dir = [(1,0), (-1,0), (0,1), (0,-1)]


def solve():
	q = queue.Queue()
	q.put(e)
	dist = [[-1 for _ in range(w)] for _ in range(h)]
	dist[e[0]][e[1]] = 0

	while not q.empty():
		(y, x) = q.get()
		#if y == s[0] and x == s[1]: #Part 1
		if map[y][x] == 'a':
			return dist[y][x]
		for (_y, _x) in dir:
			X = x+_x
			Y = y+_y
			if X >= 0 and X < w and Y >= 0 and Y < h:
				if dist[Y][X] == -1 and ord(map[Y][X]) + 1 >= ord(map[y][x]):
					dist[Y][X] = dist[y][x] + 1
					q.put((Y,X))
	#print('\n'.join(['\t'.join([str(j) for j in i]) for i in dist]))

#print('\n'.join([''.join(i) for i in map]))
print(solve())