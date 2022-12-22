from queue import Queue

valves = dict()
e = dict()
nz = []
ind = dict()

while True:
	inp = input()
	if(inp == '.'):
		break;
	inp = inp.replace(';', ' ')
	inp = inp.replace('=', ' ')
	inp = inp.replace(',', ' ')
	inp = inp.split()
	valves[inp[1]] = int(inp[5])
	if valves[inp[1]] != 0:
		ind[inp[1]] = len(nz)
		nz.append(inp[1])
	e[inp[1]] = inp[10:]

def update_dp(d, k, v):
	if k in d:
		if sum(v.values()) > sum(d[k].values()):
			d[k] = v
	else:
		d[k] = v
class State:
	def __init__(self, t, p, vis):
		self.t = t
		self.p = p
		self.vis = vis
	def __hash__(self):
		return hash((self.t, self.p, self.vis))
	def __eq__(self, other):
		return (self.t, self.p, self.vis) == (other.t, other.p, other.vis)
	def visited(self, i):
		return self.vis & (1<<ind[i]) != 0
	def set_visited(self, i):
		return self.vis | (1<<ind[i])
part = int(input('Choose part: '))
if part == 1:
	maxt = 30
else:
	maxt = 26
dp = [dict() for _ in range(maxt)] # dp[time][State]
dp[0] = {State(0,'AA',0): {}}
for t in range(maxt-1):
	for st in dp[t]:
		for v in e[st.p]:
			st2 = State(t+1, v, st.vis)
			update_dp(dp[t+1], st2, {k: v for (k,v) in dp[t][st].items()})
		if st.p in nz:
			if st.visited(st.p):
				continue
			st2 = State(t+1, st.p, st.set_visited(st.p))
			nv = {k: v for (k,v) in dp[t][st].items()}
			nv[st.p] = (maxt-1-t) * valves[st.p]
			update_dp(dp[t+1], st2, nv)
	print(f'Finished step {t} and it has {len(dp[t])} states', flush=True)

if part == 2:
	unique = list(set([tuple(sorted(d.items())) for d in dp[maxt-1].values()]))
	print(len(unique), flush=True)
	ans = 0
	for i in range(len(unique)):
		d1 = {k: v for (k,v) in unique[i]}
		for j in range(i+1, len(unique)):
			d2 = {k: v for (k,v) in unique[j]}
			d3 = dict()
			for k in list(d1.keys()) + list(d2.keys()):
				d3[k] = max(d1[k] if k in d1 else 0, d2[k] if k in d2 else 0)
			ans = max(ans, sum(d3.values()))
		if i % 10 == 0:
			print(f'Step {i} with current best ans {ans}', flush=True)
	print('Part 2: ', ans)
else:
	print('Part 1: ', max([sum(i.values()) for i in dp[maxt-1].values()]))