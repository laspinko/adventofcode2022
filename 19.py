'''
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
.
'''
import random

blueprints = []
types = ['ore', 'clay', 'obsidian', 'geode']
while True:
	inp = input()
	if inp == '.':
		break
	inp = inp.split()
	bp = {}
	bp['ore'] = {'ore': int(inp[6])}
	bp['clay'] = {'ore': int(inp[12])}
	bp['obsidian'] = {'ore': int(inp[18]), 'clay': int(inp[21])}
	bp['geode'] = {'ore': int(inp[27]), 'obsidian': int(inp[30])}
	bp['cap-ore'] = max([bp['ore']['ore'], bp['clay']['ore'], bp['obsidian']['ore'], bp['geode']['ore']])
	bp['cap-clay'] = bp['obsidian']['clay']
	bp['cap-obsidian'] = bp['geode']['obsidian']
	blueprints.append(bp)


print(blueprints)

def simulate(bp, maxt):
	def dict_tuple(d):
		return tuple(sorted(d.items()))
	class State:
		def __init__(self, res, rob, goal = None, par = None):
			self.res = res
			self.rob = rob
			self.goal = goal
			self.par = None #par
		def __repr__(self):
			return f'Resources: {str(self.res)} Robots: {str(self.rob)}' + (f' from\n{str(self.par)}' if self.par else '')
		def __hash__(self):
			return hash((dict_tuple(self.res), dict_tuple(self.rob), self.goal))
		def __eq__(self, other):
			return (dict_tuple(self.res), dict_tuple(self.rob), self.goal) == (dict_tuple(other.res), dict_tuple(other.rob), other.goal)
		def build(self, type):
			res2 = self.res.copy()
			rob2 = self.rob.copy()
			rob2[type] += 1
			for ct, cv in bp[type].items():
				res2[ct] -= cv
			return State(res2, rob2, self.goal, par = self)
		def can_build(self, type):
			return all([self.res[ct] >= cv for ct,cv in bp[type].items()])
		def try_builds_and_gather(self):
			if self.can_build(self.goal):
				return self.build(self.goal).gather_resourses(self.rob).add_goals()
			else:
				return {self.gather_resourses(self.rob)}
		def gather_resourses(self, rob):
			res2 = self.res.copy()
			rob2 = self.rob.copy()
			for ct, cv in rob.items():
				res2[ct] += cv
			return State(res2, rob2, self.goal, self)
		def add_goals(self):
			return {State(self.res.copy(), self.rob.copy(), g, par = self.par) for g in types if g == 'geode' or  bp['cap-'+g] > self.rob[g]}	
		def max_geodes(self, days): # an upper bound
			return self.min_geodes(days) + days * (days - 1) // 2
		def min_geodes(self, days): # a lower bound
			return self.res['geode'] + days * self.rob['geode']
	states = State({'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}, {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}, goal = 'ore').add_goals()
	for t in range(maxt):
		print(t, len(states), flush=True)
		next_states = set()
		ming = 0
		for st in states:
			next = list(st.try_builds_and_gather())
			#if random.randint(0, 10000) == 0:
			#	print(st,'\n','\n~~~~~~~\n','\n'.join([str(i) for i in next]),'\n=========\n', flush=True)
			
			for n in next:
				ming = max(ming, n.min_geodes(maxt-t-1))
				if n.max_geodes(maxt-t-1) >= ming:
					next_states.add(n)
		states.clear()
		for n in next_states:
			if n.max_geodes(maxt-t-1) >= ming:
				states.add(n)
	#return max([st.res['geode'] for st in states[maxt-1]])
	ans = max([st.res['geode'] for st in states])
	
	'''
	for st in states:
		if st.res['geode'] == ans:
			print(st)
			return ans
	'''
	
	return ans

if int(input('Choose part:')) == 1:
	ans = 0
	for i in range(len(blueprints)):
		mx = simulate(blueprints[i], 24)
		print(f'{i+1}/{len(blueprints)}: {mx}')
		ans += (i+1) * mx
	print(ans)
else:
	ans = 1
	for i in range(min(len(blueprints),3)):
		mx = simulate(blueprints[i], 32)
		print(f'{i+1}/{min(len(blueprints),3)}: {mx}')
		ans *= mx
	print(ans)
	