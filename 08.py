grid = []
while True:
	inp = input()
	if(inp == '.'):
		break;
	grid.append(list(map(int, inp)))

w = len(grid[0])
h = len(grid)
vis = [[False for j in range(w)] for i in range(h)]

for i in range(h):
	mx = -1
	for j in range(w):
		if j == 0 or mx < grid[i][j]:
			vis[i][j] = True;
			mx = grid[i][j]
	mx = -1
	for j in range(w-1, 0, -1):
		if j == w-1 or mx < grid[i][j]:
			vis[i][j] = True;
			mx = grid[i][j]
			
for j in range(w):
	mx = -1
	for i in range(h):
		if i == 0 or mx < grid[i][j]:
			vis[i][j] = True;
			mx = grid[i][j]
	mx = -1
	for i in range(h-1, 0, -1):
		if i == h-1 or mx < grid[i][j]:
			vis[i][j] = True;
			mx = grid[i][j]

visible = 0
for i in range(h):
	str = ''
	for j in range(w):
		if vis[i][j]:
			visible += 1
			str += '1'
		else:
			str += '0'
	print(str)

print(visible)

def score(y, x):
	ans = 1
	k = 0
	for i in range(y+1, h):
		k += 1
		if grid[i][x] >= grid[y][x]:
			break
	ans *= k
	
	k = 0
	for i in range(y-1, -1, -1):
		k += 1
		if grid[i][x] >= grid[y][x]:
			break
	ans *= k
	
	k = 0
	for j in range(x+1, w):
		k += 1
		if grid[y][j] >= grid[y][x]:
			break
	ans *= k
	
	k = 0
	for j in range(x-1, -1, -1):
		k += 1
		if grid[y][j] >= grid[y][x]:
			break
	ans *= k
	return ans

highscore = 0

for i in range(h):
	sc = ''
	for j in range(w):
		highscore = max(highscore, score(i, j))
		sc += "%s" %score(i, j)
	print(sc)
print(highscore)