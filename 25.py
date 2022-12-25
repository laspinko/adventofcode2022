def snafu_to_int(s):
	i = 0
	p = 1
	for c in s[::-1]:
		match c:
			case '-':
				d = -1
			case '=':
				d = -2
			case other:
				d = ord(c)-ord('0')
		i += p * d
		p *= 5
	return i
def int_to_snafu(i):
	if i == 0:
		return '0'
	s = ''
	while i != 0:
		if i % 5 <= 2:
			s += chr(i%5+ord('0'))
			i //= 5
		else:
			s += '-' if i % 5 == 4 else '='
			i //= 5
			i += 1
	return s[::-1]
nums = []
while True:
	inp = input()
	if inp == '':
		break
	nums.append(snafu_to_int(inp))
print(nums)
print(sum(nums))
print(int_to_snafu(sum(nums)))