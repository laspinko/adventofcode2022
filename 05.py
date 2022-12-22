cr = []
st = []
while True:
	inp = input()
	if(inp[1] == '1'):
		for i in range(1, len(inp), 4):
			str = ''
			for r in cr[::-1]:
				if r[i] == ' ':
					break;
				str += r[i]
			st.append(str)
		break
	cr.append(inp)
input()

while True:
	inp = input();
	if(inp == '.'):
		break;
	inp = inp.split()
	num = int(inp[1])
	fr = int(inp[3]) - 1
	to = int(inp[5]) - 1
	st[to] += (st[fr][-num:])
	st[fr] = st[fr][:-num]

ans = ''
for l in st:
	ans += l[-1]
print(ans)