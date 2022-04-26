N = int(input())

# 4개 미지수로 연립방정식 풀면 더럽다.
# 차라리 소인수 분해해서 가장 작은 단위 2개를 만들고 나머지 구하면 쉬울 듯.
if N < 9:
    if N == 8:
        print("2 2 2 2")
    else:
        print(-1)
    exit(0)
elif N & 1 == 0:
    N -= 4
    print("2 2 ", end="")
else:
    N -= 5
    print("2 3 ", end="")

dp = [True] * (N + 1)
primes = set()
for i in range(2, N + 1):
    if dp[i]:
        primes.add(i)
        for j in range(i, N + 1, i):
            dp[j] = False

# 3부터 탐색 시작.
for i in range(3, N, 2):
    if i in primes and N - i in primes:
        print(i, N - i)
        break