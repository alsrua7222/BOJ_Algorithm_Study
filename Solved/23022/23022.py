# 풀이 과정
# https://blog.naver.com/alsrua7222/222666592514

from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, S = map(int, input().split())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))
    arr = zip(t, v)
    arr = sorted(arr, key=lambda x: (x[0], -x[1]))
    HQ = []

    index = 0
    answer = 0
    while ((index < n) or HQ):
        # index가 배열의 길이를 초과하면 더 담을 것이 없다. 단, 힙이 존재한다면 다 비울 때 까지 정리한다.
        # 단, index가 배열의 길이보다 작다면 오름차순한 시간 순에 따라 S 이하를 만족하면 담아낸다.
        while index < n and arr[index][0] <= S:
            heappush(HQ, [-arr[index][1], arr[index][0]])
            index += 1

        # 현재 시간에 담을 수 있는 벌점이 없다면 현재 시간을 담아내는 벌점의 최초 시간으로 갱신한다.
        if not HQ:
            S = arr[index][0]
            while index < n and arr[index][0] <= S:
                heappush(HQ, [-arr[index][1], arr[index][0]])
                index += 1

        answer += (S - HQ[0][1]) * (-HQ[0][0])
        heappop(HQ)
        S += 1
        
    print(answer)