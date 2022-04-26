N = int(input())
arr = [0]
arr += list(map(int, input().split()))

# d는 메모이제이션 하는 듯?
dp = [0] * (N + 1)

# v는 값 바인딩을 해주는 듯?
v = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            v[i] = j

answer = dp[1]
# p = 0일 땐, 증가하는 수열에서 패턴을 발견하지 못할 경우 범위를 벗어남.
# 즉, p = 0은 수열에서 1번째 인덱스가 아닌 존재할 수가 없는 인덱스로 지정되어 있음.
p = 1
for i in range(1, N + 1):
    if answer < dp[i]:
        answer = dp[i]
        p = i

print(answer)

# 맨 끝에서 맨 처음까지 돌아가서 하나씩 출력하는 재귀 함수인 듯?
def go(n):
    if n == 0:
        return
    go(v[n])
    print(arr[n], end=" ")

go(p)
