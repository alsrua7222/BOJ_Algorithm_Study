import sys
input = sys.stdin.readline
 
for t in range(int(input())):
    n, f, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    f_num = arr[f - 1]
    arr.sort(reverse=True)
 
    c_f = arr[:k].count(f_num)
    t_f = arr.count(f_num)
    if c_f == 0:
        print("NO")
    elif c_f == t_f:
        print("YES")
    else:
        print("MAYBE")