import sys
input = sys.stdin.readline
for _ in range(int(input())):
    input() # empty input delete

    n, k = map(int, input().split())
    u = list(map(int, input().split()))
    dictionary = dict()
    for i, v in enumerate(u):
        if v in dictionary:
            dictionary[v].append(i)
        else:
            dictionary[v] = [i]
    
    for _ in range(k):
        a, b = map(int, input().split())
        if a not in dictionary or b not in dictionary:
            print("NO")
        else:
            path = dictionary[b][-1] - dictionary[a][0]
            print("YES" if path >= 0 else "NO")