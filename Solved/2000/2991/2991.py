A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())
AB = A + B
CD = C + D

def solve(attack, my):
    if attack >= my and my != 0:
        return 1
    return 0

PAB = P % AB
PCD = P % CD
p = 0
p += solve(A, PAB)
p += solve(C, PCD)

MAB = M % AB
MCD = M % CD
m = 0
m += solve(A, MAB)
m += solve(C, MCD)

NAB = N % AB
NCD = N % CD
n = 0
n += solve(A, NAB)
n += solve(C, NCD)

print(p)
print(m)
print(n)