# 풀이 과정
# https://blog.naver.com/alsrua7222/222701114218

N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
answer = 0
visited = [False] * N
index = 0
while index < N:
    if A[index] < 0:
        if index + 1 < N:
            if A[index + 1] <= 0:
                answer += A[index] * A[index + 1]
                visited[index] = True
                visited[index + 1] = True
                index += 2
                continue
            else:
                break
        else:
            index += 1
    else:
        break

index = N - 1
while index >= 0:
    if A[index] > 0:
        if index - 1 >= 0:
            if A[index - 1] > 1:
                answer += A[index] * A[index - 1]
                visited[index] = True
                visited[index - 1] = True
                index -= 2
                continue
            else:
                break
        else:
            index -= 1
    else:
        break

for i in range(N):
    if not visited[i]:
        answer += A[i]
print(answer)