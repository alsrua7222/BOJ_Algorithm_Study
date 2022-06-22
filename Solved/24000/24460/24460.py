N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def divide(x, y, size):
    if size == 1:
        return MAP[x][y]
    ret = []
    ret.append(divide(x, y, size // 2))
    ret.append(divide(x, y + size // 2, size // 2))
    ret.append(divide(x + size // 2, y, size // 2))
    ret.append(divide(x + size // 2, y + size // 2, size // 2))
    return sorted(ret)[1]
print(divide(0, 0, N))