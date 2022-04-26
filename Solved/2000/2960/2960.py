# 풀이 과정
# https://blog.naver.com/alsrua7222/222660341461

N, K = map(int, input().split())

prime = [True] * (N + 1)
cnt = 0
for i in range(2, N + 1):
    if prime[i]:
        for j in range(i, N + 1, i):
            if prime[j]:
                cnt += 1
                prime[j] = False
                if cnt == K:
                    print(j)
                    exit(0)
