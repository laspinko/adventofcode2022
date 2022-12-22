visited = {(0,0)}
dir = {'U': [0,-1], 'D': [0,1], 'L': [-1,0], 'R':[1,0]}

def move_tail(h, t):
	while abs(h[0]-t[0]) > 1 or  abs(h[1]-t[1]) > 1:
		if h[0] == t[0]:
			t[1] += -1 if h[1]<t[1] else 1
		else:
			t[0] += -1 if h[0]<t[0] else 1
			if h[1] != t[1]:
				t[1] += -1 if h[1]<t[1] else 1
rope = [[0,0] for i in range(10)]
steps = []
while True:
	inp = input()
	if(inp == '.'):
		break;
	inp = inp.split()
	d = dir[inp[0]]
	for i in range(int(inp[1])):
		rope[0][0] += d[0]
		rope[0][1] += d[1]
		for i in range(9):
			move_tail(rope[i], rope[i+1])
		visited.add((rope[9][0],rope[9][1]))
		steps.append((rope[9][0],rope[9][1]))
print(len(visited))
