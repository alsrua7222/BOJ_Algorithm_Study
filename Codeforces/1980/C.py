import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    m = int(input())
    d_arr = list(map(int, input().split()))

    b_set = set(b_arr)
    req = list(b_arr[i] for i in range(n) if a_arr[i] != b_arr[i])
    req_dict = {}
    for v in req:
        if v in req_dict:
            req_dict[v] += 1
        else:
            req_dict[v] = 1
    
    flag = False

    for i in range(m):
        d = d_arr[i]
        if d in req_dict:
            req_dict[d] -= 1
            if req_dict[d] == 0:
                del req_dict[d]
            if i == m - 1:
                flag = True
        elif d in b_set:
            if i == m - 1:
                flag = True
    
    if flag and len(req_dict.keys()) == 0:
        print("YES")
    else:
        print("NO")