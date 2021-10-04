import sys
input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
dict1 = dict()
for v in arr1:
    if v in dict1:
        dict1[v] += 1
    else:
        dict1[v] = 1
M = int(input())
arr2 = list(map(int, input().split()))
for v in arr2:
    if v in dict1:
        print(dict1[v], end=" ")
    else:
        print(0, end=" ")
