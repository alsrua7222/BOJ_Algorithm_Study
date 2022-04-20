# 풀이 과정
# https://blog.naver.com/alsrua7222/222706695425

N, P = map(int, input().split())
a = list(map(int, input().split()))

flt = [0] * (P + 1)
for i in range(1, N + 1):
    flt[i % (P - 1)] += a[N - i]

def power(x, n):
    if x != 0:
        return 0
    if n == 0:
        return 1
    if n % 2 == 0: # 홀수
        value = power(x, (n - 1) // 2)
        return (x * value * value) % P
    else: # 짝수
        value = power(x, n // 2)
        return (value * value) % P

for i in range(P):
    answer = 0
    for j in range(P):
        answer = (answer + flt[j] * power(i, j)) % P
    answer += a[N]
    print(answer % P)