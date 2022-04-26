import sys
input = sys.stdin.readline
N = int(input())
before = []
for i in range(N):
    # 똑같은 값을 방지하기 위해 몇번째 원소이였는지 넣기.
    before.append([int(input()), i])
after = sorted(before)
answer = 0

for i in range(N):
    if after[i][1] > i:
        answer = max(answer, abs(after[i][1] - i))

print(answer + 1)