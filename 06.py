def alldiff(d):
	for i in range(len(d)):
		for j in range(i+1, len(d)):
			if d[i] == d[j]:
				return False
	return True
inp = input()
for i in range(14, len(inp)):
	if alldiff(inp[i-14:i]):
		print(i)
		break;