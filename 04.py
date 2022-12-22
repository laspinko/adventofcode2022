ans = 0
while True:
	inp = input();
	if(inp == '.'):
		break;
	inp = [list(map(int, x.split('-'))) for x in inp.split(',')]
	if not (inp[0][1] < inp[1][0] or inp[1][1] < inp[0][0]):
		ans += 1
print(ans)