from sys import stdin
mx = 0
curr = 0
totals = []
while True:
	n = input();
	if(n == '.'):
		break;
	if n == '':
		totals.append(curr)
		curr = 0;
	else:
		curr += int(n)
totals.sort();
print(totals[-1]+totals[-2]+totals[-3])