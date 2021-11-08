import math, sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
MAX, MIN = 10**6 + 1, -1
tree = [[MAX, MIN] for _ in range((1 << (math.ceil(math.log2(N)) + 1)))]

def init(start, end, here):
    if start == end:
        tree[here][0] = min(arr[start], tree[here][0])
        tree[here][1] = max(arr[start], tree[here][1])
        return tree[here]
    mid = (start + end) // 2
    tmp1 = init(start, mid, here * 2)
    tmp2 = init(mid + 1, end, here * 2 + 1)
    tree[here][0] = min(tree[here][0], tmp1[0], tmp2[0])
    tree[here][1] = max(tree[here][1], tmp1[1], tmp2[1])
    return tree[here]

def query(start, end, here, left, right):
    if right < start or end < left:
        return [MAX, MIN]
    if left <= start and end <= right:
        return tree[here]
    mid = (start + end) // 2
    tmp1 = query(start, mid, here * 2, left, right)
    tmp2 = query(mid + 1, end, here * 2 + 1, left, right)
    return [min(tmp1[0], tmp2[0]), max(tmp1[1], tmp2[1])]

init(0, N - 1, 1)
for _ in range(M):
    s, e = map(int, input().split())
    mm, mx = query(0, N - 1, 1, s - 1, e - 1)
    print(mx - mm)
