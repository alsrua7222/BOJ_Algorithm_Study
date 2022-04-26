import sys
sys = sys.stdin.readline
def CCW(a, b, c):
    tmp1 = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    tmp2 = b[0] * a[1] + c[0] * b[1] + a[0] * c[1]
    result = abs(tmp1 - tmp2) / 2
    return result

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.append(arr[0])
answer = 0
for i in range(N):
    answer += arr[i][0] * arr[i + 1][1]
    answer -= arr[i][1] * arr[i + 1][0]
print(round(abs(answer) / 2, 1))
