import sys; input = sys.stdin.readline
N = int(input())
signs = [0] * (N + 1)
for i in range(1, N + 1):
    query = input().split()
    if len(query) == 1:
        signs[i] = -1
    else:
        signs[i] = int(query[1])

cancleds = [True] * (N + 1)
for i in range(N, 0, -1):
    if cancleds[i] and signs[i] != -1:
        cancleds[signs[i]] = False

answer = []
for i in range(1, N + 1):
    if cancleds[i]:
        answer.append(i)

print(len(answer))
print(*answer)