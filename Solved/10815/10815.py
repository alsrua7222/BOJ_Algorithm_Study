# 풀이 과정
# https://blog.naver.com/alsrua7222/222603749026

N = int(input())
A = set(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
answer = []
for v in B:
    answer.append(1 if v in A else 0)
print(*answer)
