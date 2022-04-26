import math
str1 = input()
def isPelindrom(s):
	if len(s) == 1:
		return True
	for i in range(len(s) // 2):
		if s[i] != s[-(i + 1)]:
			return False
	if not isPelindrom(s[:len(s)//2]) or not isPelindrom(s[int(math.ceil(len(s)/2)):]):
		return False
	return True
if isPelindrom(str1):
	print("AKARAKA")
else:
	print("IPSELENTI")
