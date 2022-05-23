import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    A = max(a)
    B = max(b)
    if A >= B:
        print('Alice')
    else:
        print('Bob')
    
    if A <= B:
        print('Bob')
    else:
        print('Alice')