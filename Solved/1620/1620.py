import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict1 = dict()
for i in range(1, N + 1):
    tmp = input().rstrip()
    dict1[tmp] = i
    dict1[i] = tmp

for _ in range(M):
    query = input().rstrip()
    if query.isdecimal():
        print(dict1[int(query)])
    else:
        print(dict1[query])
