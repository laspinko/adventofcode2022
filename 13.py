import ast

def cmp(a, b): # is a strictly less than b
	if isinstance(a, int) and isinstance(b, int):
		return a < b
	if isinstance(a, int) and not isinstance(b, int):
		return cmp([a], b)
	if not isinstance(a, int) and isinstance(b, int):
		return cmp(a, [b])
	for i in range(min(len(a), len(b))):
		if cmp(a[i], b[i]):
			return True
		if cmp(b[i], a[i]):
			return False
	return len(a) < len(b)

div = [[[2]], [[6]]]
lt = [1,2]
ans = 0
while True:
	a = ''
	while a == '':
		a = input()
	if(a == '.'):
		break;
	for i in range(2):
		if cmp(eval(a), div[i]):
			lt[i] += 1
print(lt[0] * lt[1])