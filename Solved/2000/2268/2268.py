import math, sys
input = sys.stdin.readline
N, M = map(int, input().split())
h = math.ceil(math.log2(N))
arr = [0] * (N + 1)
tree = [0] * (1 << (h + 1))

def update(start, end, here, index, diff):
    if index < start or end < index:
        return
    tree[here] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, here * 2, index, diff)
        update(mid + 1, end, here * 2 + 1, index, diff)
    return

def query(start, end, here, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[here]
    mid = (start + end) // 2
    return query(start, mid, here * 2, left, right) + query(mid + 1, end, here * 2 + 1, left, right)

for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        if cmd[1] > cmd[2]:
            cmd[1], cmd[2] = cmd[2], cmd[1]
        print(query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1))
    else:
        diff = cmd[2] - arr[cmd[1] - 1]
        arr[cmd[1] - 1] = cmd[2]
        update(0, N - 1, 1, cmd[1] - 1, diff)
