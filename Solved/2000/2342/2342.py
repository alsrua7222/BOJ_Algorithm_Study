# 풀이 과정
# https://blog.naver.com/alsrua7222/222654774307

import sys
sys.setrecursionlimit(10 ** 6)

query = list(map(int, input().split()))
query.pop()
chache = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(len(query) + 1)]

def calc(_from, _to):
    if _from == _to:
        return 1
    
    if _from == 0:
        return 2
    
    if abs(_from - _to) == 2:
        return 4
    else:
        return 3

def backtracking(left, right, cnt):
    if cnt == len(query):
        return 0
    if chache[cnt][left][right] != 0:
        return chache[cnt][left][right]
    chache[cnt][left][right] = min(
        calc(left, query[cnt]) + backtracking(query[cnt], right, cnt + 1), 
        calc(right, query[cnt]) + backtracking(left, query[cnt], cnt + 1)
    )
    return chache[cnt][left][right]

print(backtracking(0, 0, 0))