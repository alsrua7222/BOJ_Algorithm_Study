for _ in range(int(input())):
    n = int(input())
    string = list(input())
    query = list(input())
    c = set(query[1:])
    
    cur = -1
    MAX = -1
    for i in range(n - 1, -1, -1):
        if string[i] in c:
            MAX = max(MAX, cur + 1)
            cur = 0
        else:
            if cur == -1:
                continue
            cur += 1
            MAX = max(MAX, cur)
 
    if MAX == -1:
        print(0)
    else:
        print(MAX)