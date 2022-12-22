import queue

dropplets = set()
mx = 0
while True:
	inp = input()
	if inp == '.':
		break
	inp = inp.split(',')
	inp = tuple([int(i) for i in inp])
	dropplets.add(inp)
	mx = max(mx, inp[0], inp[1], inp[2])
dir = [
	[1,0,0],
	[-1,0,0],
	[0,1,0],
	[0,-1,0],
	[0,0,1],
	[0,0,-1],
]
def steam_fill(pos):
	seen = set()
	q = queue.Queue()
	q.put(pos)
	seen.add(tuple(pos))
	ans = 0
	while not q.empty():
		p = q.get()
		#print(p)
		for d in dir:
			p2 = [p[i] + d[i] for i in range(3)]
			if all([i >= -1 and i <= mx+1 for i in p2]):
				if tuple(p2) not in dropplets:
					if tuple(p2) not in seen:
						q.put(p2)
						seen.add(tuple(p2))
				else:
					ans += 1
	return ans

if int(input('Choose part:')) == 1:
	ans = 0
	for d in dropplets:
		for _d in dir:
			n = tuple([d[i] + _d[i] for i in range(3)])
			if n not in dropplets:
				ans += 1
	print(ans)
else:
	print(steam_fill([-1,-1,-1]))