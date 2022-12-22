ori = []
num = []
index = []
ind0 = None
while True:
	inp = input()
	if inp == '.':
		break
	inp = int(inp)
	ind = len(index)
	if inp == 0:
		ind0 = ind
	index.append(ind)
	num.append((inp, ind))
n = len(num)
print('n =', n)

def move(ind, offset):
	global num, index
	'''offset %= (n-1)
	while offset+ind >= n:
		print('a')
		offset -= n-1'''
	target = (ind+offset)%(n-1)
	dir = 1 if target >= ind else -1
	for i in range(ind, target, dir):
		index[num[i][1]], index[num[i+dir][1]] = index[num[i+dir][1]], index[num[i][1]]
		num[i], num[i+dir] = num[i+dir], num[i]

if int(input('Choose part:')) == 1:
	for i in range(n):
		ind = index[i]
		#print(f'Round {i}: moving {num[index[i]][0]} steps')
		move(ind, num[ind][0])
		#print([(a,b) for a,b in num])
else:
	for i in range(n):
		num[i] = (num[i][0]*811589153, num[i][1])
	for step in range(10):	
		print('Step', step, flush=True)
		for i in range(n):
			ind = index[i]
			move(ind, num[ind][0])
a = num[(index[ind0]+1000)%n][0]
b = num[(index[ind0]+2000)%n][0]
c = num[(index[ind0]+3000)%n][0]
ans = a+b+c
print(a, b, c, ans)