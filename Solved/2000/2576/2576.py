answer = 0
MIN = 987654320
for i in range(7):
	tmp = int(input())
	if tmp % 2 == 1:
		answer += tmp
		MIN = min(MIN, tmp)
if MIN == 987654320:
	print(-1)
else:
	print(answer, MIN, sep="\n")
