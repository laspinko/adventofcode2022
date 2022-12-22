tree = {'/': {'$size': 0}}
tree['/']['..'] = tree
curr = tree['/']

def update_size(d, nf):
	c = d
	while not c.get('/'):
		c['$size'] += nf
		c = c['..']
while True:
	inp = input();
	if(inp == '.'):
		break;
	inp = inp.split()
	if inp[0] == '$':
		if inp[1] == 'cd':
			if inp[2] == '/':
				curr = tree['/']
			else:
				if curr.get(inp[2]):
					curr = curr[inp[2]]
				else:
					curr[inp[2]] = {'..': curr, '$size': 0}
					curr = curr[inp[2]]
	elif inp[0] != 'dir':
		if not curr.get(inp[1]):
			curr[inp[1]] = {'$size': inp[0]}
			update_size(curr, int(inp[0]))

def get_sum_sizes(d):
	ans = 0
	if not d.get('..'):
		return 0
	if d['$size'] < 100000:
		ans += d['$size']
	for i in d:
		if i != '$size' and i != '..':
			ans += get_sum_sizes(d[i])
	return ans
def find_smallest(d, mn):
	ans = 70000000
	if not d.get('..'):
		return 70000000
	if d['$size'] >= mn:
		ans = d['$size']
	for i in d:
		if i != '$size' and i != '..':
			ans = min(ans, find_smallest(d[i], mn))
	return ans
def print_tree(d, depth, name):
	print(depth + name + ': ', d['$size'])
	for i in d:
		if i != '$size' and i != '..':
			print_tree(d[i], depth + ' ', i)
print_tree(tree['/'], '', '/')
print('sum ', get_sum_sizes(tree['/']))
print('smallest ',find_smallest(tree['/'], 30000000 - (70000000 - tree['/']['$size'])))