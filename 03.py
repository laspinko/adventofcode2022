ans = 0
def priority(l):
	if ord(l) < ord('a'):
		return ord(l) - ord('A') + 27
	else:
		return ord(l) - ord('a') + 1
"""
while True:
	inp = input();
	if inp == '.':
		break;
	dict = {}
	for l in inp[0 : len(inp)//2]:
		dict[l] = True
	for l in inp[len(inp)//2 :]:
		if dict.get(l):
			ans += priority(l)
			break;
print(ans)
"""


while True:
	inp = ['','','']
	inp[0] = input();
	if inp[0] == '.':
		break;
	inp[1], inp[2] = input(), input()
	dict = {}
	for i in range(3):
		for l in inp[i]:
			if dict.get(l):
				dict[l][i] = True
			else:
				dict[l] = {i: True}
	for l in dict:
		if dict[l].get(0) and dict[l].get(1) and dict[l].get(2):
			ans += priority(l)
print(ans)