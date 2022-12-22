score = 0
while True:
	inp = input();
	if(inp == '.'):
		break;
	oponent = ord(inp[0])-ord('A')
	if inp[2] == 'X':
		me = (oponent + 2) % 3
	elif inp[2] == 'Y':
		me = oponent
	else:
		me = (oponent+1)%3
	score += me + 1
	if(me == oponent):
		score += 3
	elif (oponent+1)%3==me:
		score += 6
print(score)