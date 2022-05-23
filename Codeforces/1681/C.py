import sys
input = sys.stdin.readline
def Issorted(arr):
    pre = arr[0]
    for v in arr[1:]:
        if pre > v:
            return False
        pre = v
    return True

def correct(answer):
    print(len(answer))
    for v in answer:
        print(*v)
    return

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    aa = a.copy()
    ab = b.copy()
    answerA = []
    for i in range(n):
        for j in range(i + 1, n):
            if aa[i] >= aa[j]:
                if aa[i] == aa[j] and ab[i] <= ab[j]:
                    continue
                aa[i], aa[j] = aa[j], aa[i]
                ab[i], ab[j] = ab[j], ab[i]
                answerA.append((i + 1, j + 1))
    
    if Issorted(aa) and Issorted(ab):
        correct(answerA)
        continue

    aa = a.copy()
    ab = b.copy()
    answerB = []
    for i in range(n):
        for j in range(i + 1, n):
            if ab[i] >= ab[j]:
                if ab[i] == ab[j] and aa[i] <= aa[j]:
                    continue
                ab[i], ab[j] = ab[j], ab[i]
                aa[i], aa[j] = aa[j], aa[i]
                answerB.append((i, j))
    
    if Issorted(aa) and Issorted(ab):
        correct(answerB)
    else:
        print(-1)