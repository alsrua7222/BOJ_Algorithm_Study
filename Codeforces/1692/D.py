import sys
input = sys.stdin.readline

def IsPalindrome(s):
    return s == s[::-1]

def getTimes(s, t):
    tmp = s.split(":")
    h = int(tmp[0])
    m = int(tmp[1])
    
    if m + t > 59:
        h += (m + t) // 60
        m = (m + t) % 60
    else:
        m += t
    
    if h > 23:
        h = h % 24
    
    str_h = str(h) if h >= 10 else "0" + str(h)
    str_m = str(m) if m >= 10 else "0" + str(m)

    return str_h + ":" + str_m


for _ in range(int(input())):
    query = input().split()
    s = query[0]
    x = int(query[1])
    answer = 0
    used = set()
    while True:
        if s in used:
            break
        if IsPalindrome(s):
            answer += 1
        used.add(s)
        s = getTimes(s, x)
    print(answer)