import sys, math
sys.setrecursionlimit(10**5)

# https://www.acmicpc.net/problem/17475

MAX = 10 ** 9 + 7
MIN = -MAX
N = int(input())
A = list(map(int, input().split()))
B = A.copy()
C = A.copy()
h = int(math.ceil(math.log2(N))) + 1
tree = [0] * (1 << h)
lazy = [0] * (1 << h)
treeMin = [MAX] * (1 << h)
lazyMin = [MAX] * (1 << h)
treeMax = [MIN] * (1 << h)
lazyMax = [MIN] * (1 << h)

def propagate(start, end, here):
    if lazy[here] > 0:
        tree[here] += (end - start + 1) * lazy[here]
        if start != end:
            lazy[here * 2] += lazy[here]
            lazy[here * 2 + 1] += lazy[here]
        lazy[here] = 0

def propagateMin(start, end, here):
    if lazy[here] != MAX:
        tree[here] = min(tree[here], lazy[here])
        if start != end:
            lazy[here * 2] = min(lazy[here * 2], lazy[here])
            lazy[here * 2 + 1] = min(lazy[here * 2 + 1], lazy[here])
        lazy[here] = MAX


def propagateMax(start, end, here):
    if lazy[here] != MIN:
        tree[here] = max(tree[here], lazy[here])
        if start != end:
            lazy[here * 2] = max(lazy[here * 2], lazy[here])
            lazy[here * 2 + 1] = max(lazy[here * 2 + 1], lazy[here])
        lazy[here] = MIN


def propagateB(start, end, here):
    if lazyMin[here] != MAX:
        treeMin[here] = min(treeMin[here], lazyMin[here])
        if start != end:
            lazyMin[here * 2] = min(lazyMin[here * 2], lazyMin[here])
            lazyMin[here * 2 + 1] = min(lazyMin[here * 2 + 1], lazyMin[here])
        lazyMin[here] = MAX

def propagateC(start, end, here):
    if lazyMax[here] != MIN:
        treeMax[here] = max(treeMax[here], lazyMax[here])
        if start != end:
            lazyMax[here * 2] = max(lazyMax[here * 2], lazyMax[here])
            lazyMax[here * 2 + 1] = max(lazyMax[here * 2 + 1], lazyMax[here])
        lazyMax[here] = MIN


def updateMax(start, end, here, left, right, value):
    propagateMax(start, end, here)
    if start > right or left > end:
        return
    # tree[here] = max(tree[here], value)
    # if start == end:
    #     return
    if left <= start and end <= right:
        tree[here] = max(tree[here], value)
        if start != end:
            lazy[here * 2] = max(tree[here], lazy[here * 2])
            lazy[here * 2 + 1] = max(tree[here], lazy[here * 2 + 1])
        return
    mid = (start + end) // 2
    updateMax(start, mid, here * 2, left, right, value)
    updateMax(mid + 1, end, here * 2 + 1, left, right, value)
    return

def updateMaxC(start, end, here, left, right):
    propagateC(start, end, here)
    if start > right or left > end:
        return
    # treeMax[here] = max(treeMax[here], tree[here])
    # if start == end:
    #     return
    if left <= start and end <= right:
        treeMax[here] = max(treeMax[here], tree[here])
        if start != end:
            lazy[here * 2] = max(treeMax[here], lazy[here * 2])
            lazy[here * 2 + 1] = max(treeMax[here], lazy[here * 2 + 1])
        return
    mid = (start + end) // 2
    updateMaxC(start, mid, here * 2, left, right)
    updateMaxC(mid + 1, end, here * 2 + 1, left, right)
    treeMax[here] = max(treeMax[here * 2], treeMax[here * 2 + 1])
    return

def updateMin(start, end, here, left, right, value):
    propagateMin(start, end, here)
    if start > right or left > end:
        return
    # tree[here] = min(tree[here], value)
    # if start == end:
    #     return
    if left <= start and end <= right:
        tree[here] = min(tree[here], value)
        if start != end:
            lazy[here * 2] = min(tree[here], lazy[here * 2])
            lazy[here * 2 + 1] = min(tree[here], lazy[here * 2 + 1])
        return
    mid = (start + end) // 2
    updateMin(start, mid, here * 2, left, right, value)
    updateMin(mid + 1, end, here * 2 + 1, left, right, value)
    tree[here] = min(tree[here * 2], tree[here * 2 + 1])
    return

def updateMinB(start, end, here, left, right):
    propagateB(start, end, here)
    if start > right or left > end:
        return
    # treeMin[here] = min(treeMin[here], tree[here])
    # if start == end:
    #     return
    if left <= start and end <= right:
        treeMin[here] = min(treeMin[here], tree[here])
        if start != end:
            lazyMin[here * 2] = min(treeMin[here], lazyMin[here * 2])
            lazyMin[here * 2 + 1] = min(treeMin[here], lazyMin[here * 2 + 1])
        return
    mid = (start + end) // 2
    updateMinB(start, mid, here * 2, left, right)
    updateMinB(mid + 1, end, here * 2 + 1, left, right)
    treeMin[here] = min(treeMin[here * 2], treeMin[here * 2 + 1])
    return

def updateAdd(start, end, here, left, right, diff):
    propagate(start, end, here)
    if start > right or left > end:
        return
    # tree[here] += diff
    # if start == end:
    #     return
    if left <= start and end <= right:
        tree[here] += diff

        if start != end:
            lazy[here * 2] += diff
            lazy[here * 2 + 1] += diff
        return
    mid = (start + end) // 2
    updateAdd(start, mid, here * 2, left, right, diff)
    updateAdd(mid + 1, end, here * 2 + 1, left, right, diff)
    tree[here] = max(tree[here * 2], tree[here * 2 + 1])
    return

def queryA(start, end, here, left, right):
    propagate(start, end, here)
    if start > right or end < left:
        return MAX
    if left <= start and end <= right:
        return tree[here]
    mid = (start + end) // 2
    l = queryA(start, mid, here * 2, left, right)
    r = queryA(mid + 1, end, here * 2 + 1, left, right)
    return min(l, r)

def queryB(start, end, here, left, right):
    propagateB(start, end, here)
    if start > right or end < left:
        return MAX
    if left <= start and end <= right:
        return treeMin[here]
    mid = (start + end) // 2
    l = queryB(start, mid, here * 2, left, right)
    r = queryB(mid + 1, end, here * 2 + 1, left, right)
    return min(l, r)

def queryC(start, end, here, left, right):
    propagateC(start, end, here)
    if start > right or end < left:
        return MIN
    if left <= start and end <= right:
        return treeMax[here]
    mid = (start + end) // 2
    l = queryC(start, mid, here * 2, left, right)
    r = queryC(mid + 1, end, here * 2 + 1, left, right)
    return max(l, r)

for i in range(len(A)):
    updateMax(i, i, i + 1, i, i, A[i])
    updateMaxC(i, i, i + 1, i, i)
    updateMinB(i, i, i + 1, i, i)

for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        updateAdd(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1, cmd[3])
    elif cmd[0] == 2:
        updateMax(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1, cmd[3])
    elif cmd[0] == 3:
        updateMin(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1, cmd[3])
    elif cmd[0] == 4:
        print(queryA(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1))
    elif cmd[0] == 5:
        print(queryB(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1))
    elif cmd[0] == 6:
        print(queryC(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1))

    updateMinB(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)
    updateMaxC(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)
    print(f"tree = {tree}")
    print(f"treeMin = {treeMin}")
    print(f"treeMax = {treeMax}")




