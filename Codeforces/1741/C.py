import sys
input = sys.stdin.readline

def getMyDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList
        
for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    answer = n
    SUM = sum(a)
    for v in getMyDivisor(SUM):
        req = SUM / v
        flag = True

        s = 0
        length = 0

        MAX = 0
        for i in range(n):
            s += a[i]
            length += 1

            if s == req:
                MAX = max(length, MAX)
                s = 0
                length = 0
            elif s > req:
                flag = False
                break
        if flag:
            answer = min(answer, MAX)
    print(answer)