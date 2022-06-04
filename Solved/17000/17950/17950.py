import sys
input = sys.stdin.readline
H, x = map(int, input().split())
answer = 0
inc_x = x
for _ in range(H):
    answer = (answer + int(input()) * inc_x) % 1000000007
    inc_x = (inc_x * x) % 1000000007
print(answer)