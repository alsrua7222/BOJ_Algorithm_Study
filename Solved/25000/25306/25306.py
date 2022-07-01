A, B = map(int, input().split())

def getXOR(n):
    mod = n % 4
    if mod == 0:
        return n
    if mod == 1:
        return 1
    if mod == 2:
        return n + 1
    return 0

print(getXOR(A - 1) ^ getXOR(B))