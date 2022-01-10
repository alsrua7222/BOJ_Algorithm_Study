import sys
input = sys.stdin.readline
N, M = map(int, input().split())
set1 = set()
for _ in range(N):
    set1.add(input().rstrip())
answer = []
for _ in range(M):
    tmp = input().rstrip()
    if tmp in set1:
        answer.append(tmp)
answer = sorted(answer)
print(len(answer))
print(*answer, sep="\n")
