# 풀이 과정
# https://blog.naver.com/alsrua7222/222654100894

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
arr = [input().rstrip() for _ in range(n)]
hash = set()
visited = [0] * n


def backtracking(collect):
    if len(collect) == k:
        tmp = ''.join(collect)
        if tmp not in hash:
            hash.add(tmp)

        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        backtracking(collect + [arr[i]])
        visited[i] = False
    return


backtracking([])
print(len(hash))