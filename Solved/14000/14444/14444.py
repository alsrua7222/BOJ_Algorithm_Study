# 풀이 과정
# https://blog.naver.com/alsrua7222/222635507930

import sys
input = sys.stdin.readline

def manacher(dp, str1, len):
    rad = 0
    cen = 0
    for i in range(len):
        if i <= rad:
            dp[i] = min(rad - i, dp[2 * cen - i])
        else:
            dp[i] = 0
        while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len and str1[i - dp[i] - 1] == str1[i + dp[i] + 1]:
            dp[i] += 1
        if rad < i + dp[i]:
            rad = i + dp[i]
            cen = i
    return

str1 = list(input().rstrip())
str2 = "."
for v in str1:
    str2 += v + "."
dp = [0] * len(str2)

manacher(dp, str2, len(str2))
print(max(dp))