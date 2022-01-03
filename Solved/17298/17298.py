# 풀이 과정
# https://blog.naver.com/alsrua7222/222612171433
N = int(input())
arr = list(map(int, input().split()))

stack = []
answer = [-1] * N
for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        answer[stack.pop()[1]] = arr[i]
    stack.append([arr[i], i])

print(*answer)
