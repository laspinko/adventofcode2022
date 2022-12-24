import heapq
import math
import progressbar
import time

class PriorityQueue:
	def __init__(self):
		self._pq = []
		self._index = 0
	
	def put(self, item, priority):
		heapq.heappush(self._pq, (priority, self._index, item))
		self._index += 1
	def get(self):
		return heapq.heappop(self._pq)[-1]
	def empty(self):
		return len(self._pq)==0
def dist(a,b):
	return abs(a[0]-b[0])+abs(a[1]-b[1])
def add(a,b):
	return (a[0]+b[0],a[1]+b[1])
dir = {'^':(0,-1), 'v':(0,1), '<':(-1,0), '>':(1,0), 'o': (0,0)}

w = 0
h = 0
class Blizzard:
	def __init__(self, x, y, d):
		self.x = x
		self.y = y
		self.d = d
		self.dir = dir[d]
	def collision(self, x, y, t):
		return x==(self.x+self.dir[0]*t-1)%w+1 and y==(self.y+self.dir[1]*t-1)%h+1
	def get_pos(self,t):
		return ((self.x+self.dir[0]*t-1)%w+1,(self.y+self.dir[1]*t-1)%h+1)
blizzards = []

map = []
while True:
	inp = input()
	if inp == '':
		break
	y = len(map)
	map.append(inp)
	for x in range(len(inp)):
		if inp[x] in dir.keys():
			blizzards.append(Blizzard(x,y,inp[x]))
w = len(map[0])-2
h = len(map)-2
cycle = math.lcm(w,h)

precomputed = []
for t in range(cycle):
	precomputed.append({})
	for i in blizzards:
		pos = i.get_pos(t)
		if pos not in precomputed[t]:
			precomputed[t][pos] = []
		precomputed[t][pos].append(i.d)

def draw_blizzards(b):
	m = [[(b[(x,y)][0] if len(b[(x,y)])==1 else chr(len(b[(x,y)])+ord('0'))) if (x,y) in b else '.' for x in range(1,w+1)] for y in range(1,h+1)]
	print('\n'.join([''.join(i) for i in m]), flush=True)
def animate_blizzards():
	for p in precomputed:
		draw_blizzards(p)
		time.sleep(0.5)
		print("\033[A\033[K"*h, end="")
def in_map(p):
	if p[0] < 0 or p[0]>w+1 or p[1] < 0 or p[1]>h+1:
		return False
	return map[p[1]][p[0]] != '#'
def valid(p, t):
	return in_map(p) and p not in precomputed[t%cycle]
def find_path(s,f, init_t = 0):
	q = PriorityQueue()
	
	q.put((s,init_t, []), dist(s, f))
	seen = {(s,init_t%cycle)}
	steps = 0
	#with progressbar.NonInteractiveUpdateProgressBar(max_value=(w*h+2)*cycle) as bar:
	while not q.empty():
		pos, t, hist = q.get()
		#bar.update(bar.value+1)
		steps += 1
		if steps % 1000 == 0:
			print(f'{steps}/{cycle*(w*h+2)}', flush=True)
		#print(pos, t)
		if pos == f:
			#print(hist)
			return t
		for (dn,d) in dir.items():
			pos2 = add(pos, d)
			if valid(pos2, t+1) and (pos2, (t+1)%cycle) not in seen:
				q.put((pos2, t+1, hist+[dn]), t+1+dist(pos2, f))
				seen.add((pos2,(t+1)%cycle))

s, f = (1,0), (w,h+1)
if int(input('Choose part:')) == 1:
	print(find_path(s,f))
else:
	print(find_path(s,f,find_path(f,s,find_path(s,f))))

if input('Play animation?(y/n)') == 'y':
	animate_blizzards()