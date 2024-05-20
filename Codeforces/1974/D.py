import sys
input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = input().strip()

    #동서남북
    xy = [0, 0, 0, 0]
    for c in s:
        if c  == 'E':
            xy[0] += 1
        if c == 'W':
            xy[1] += 1
        if c == 'S':
            xy[2] += 1
        if c == 'N':
            xy[3] += 1

    if sum(xy) == 0 or sum([r//2 for r in xy]) == 0:
        print("NO")
    else:
        E = [xy[0] // 2, xy[0] - xy[0] // 2]
        W = [xy[1] // 2, xy[1] - xy[1] // 2]
        S = [xy[2] // 2, xy[2] - xy[2] // 2]
        N = [xy[3] // 2, xy[3] - xy[3] // 2]
        
        s1 = ['R'] * n
        r, h = 0, 0
        for i in range(n):
            if s[i] == 'E':
                if E[0] > 0:
                    E[0] -= 1
                    s1[i] = 'R'
                    r += 1
                else:
                    E[1] -= 1
                    s1[i] = 'H'
                    h += 1
            elif s[i] == 'W':
                if W[0] > 0:
                    W[0] -= 1
                    s1[i] = 'R'
                    r += 1
                else:
                    W[1] -= 1
                    s1[i] = 'H'
                    h += 1
            elif s[i] == 'S':
                if S[0] > 0:
                    S[0] -= 1
                    s1[i] = 'R'
                    r += 1
                else:
                    S[1] -= 1
                    s1[i] = 'H'
                    h += 1
            else:
                if N[0] > 0:
                    N[0] -= 1
                    s1[i] = 'R'
                    r += 1
                else:
                    N[1] -= 1
                    s1[i] = 'H'
                    h += 1
        if r == 0 or h == 0:
            print("NO")
        else:
            print(s1)
