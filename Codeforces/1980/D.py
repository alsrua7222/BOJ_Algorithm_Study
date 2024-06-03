import sys
input = sys.stdin.readline

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    b_arr = [gcd(arr[i], arr[i + 1]) for i in range(n - 1)]
    
    flag = True
    cur = 0
    for i in range(n - 2):
        if b_arr[i] > b_arr[i + 1]:
            flag = False
            cur = i
            break
    
    if flag:
        print("YES")
        continue

    def check(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True
    
    a1 = [arr[i] for i in range(n) if i != cur + 1]
    a2 = [arr[i] for i in range(n) if i != cur + 2]
    a3 = [arr[i] for i in range(n) if i != cur]

    result_arr = [gcd(a1[i], a1[i + 1]) for i in range(len(a1) - 1)]
    flag1 = check(result_arr)
    result_arr = [gcd(a2[i], a2[i + 1]) for i in range(len(a2) - 1)]
    flag2 = check(result_arr)
    result_arr = [gcd(a3[i], a3[i + 1]) for i in range(len(a3) - 1)]
    flag3 = check(result_arr)
    
    if not (flag1 or flag2 or flag3):
        print("NO")
    else:
        print("YES")