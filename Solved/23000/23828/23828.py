# 풀이 과정
# https://blog.naver.com/alsrua7222/222598846154

N, M = map(int, input().split())
arr = list(map(int, input().split()))
count = dict()

for v in arr:
    if v not in count:
        count[v] = 1
    else:
        count[v] += 1

keys = sorted(count.keys())
dp = [[0 for col in range(len(keys))] for row in range(M)]
dp[0][0] = keys[0] * count[keys[0]]
for i in range(1, len(keys)):
    dp[0][i] = dp[0][i - 1] + keys[i] * count[keys[i]]

for row in range(1, M):
    for col in range(row, len(keys)):
        dp[row][col] = (dp[row][col - 1] + keys[col] * count[keys[col]] * dp[row - 1][col - 1]) % 1000000007

print(dp[-1][-1])
