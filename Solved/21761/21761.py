# 풀이 과정
# https://blog.naver.com/alsrua7222/222656071826

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
cards = [[] for _ in range(4)]

for _ in range(N):
    ch, n = input().split()
    cards[ord(ch) - ord('A')].append(int(n))

for i in range(4):
    cards[i].sort()

def mul(arr):
    res = 1
    for v in arr:
        res *= v
    return res

MAX = mul(arr)
for _ in range(K):
    idx = -1
    for i in range(4):
        if cards[i]:
            arr[i] += cards[i][-1]
            tmp = mul(arr)
            arr[i] -= cards[i][-1]
            if MAX < tmp:
                MAX = tmp
                idx = i
    arr[idx] += cards[idx][-1]
    print(chr(idx + ord('A')), cards[idx].pop())