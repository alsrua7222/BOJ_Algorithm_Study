# 풀이 과정
# https://blog.naver.com/alsrua7222/222701988565

from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))
answer = [0] * N

Deque = deque()
for i in range(N):
    while Deque and Deque[0] < i - L + 1:
        Deque.popleft()
    while Deque and A[Deque[-1]] >= A[i]:
        Deque.pop()
    
    Deque.append(i)
    answer[i] = A[Deque[0]]
print(*answer)