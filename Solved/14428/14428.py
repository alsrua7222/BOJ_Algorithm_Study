import math, sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
h = math.ceil(math.log2(N))

# 이진트리의 높이 = log base: 2, x: N을 올림한 값이랑 같다.
# 값과 인덱스 트리를 추가.
tree = [0] * (1 << (h + 1))
tree_index = [0] * (1 << (h + 1))


def init(start, end, here):
    if start == end:
        tree[here] = arr[start]
        tree_index[here] = start
        return [tree[here], tree_index[here]]
    mid = (start + end) // 2
    tmp1 = init(start, mid, here * 2)
    tmp2 = init(mid + 1, end, here * 2 + 1)
    if tmp1[0] < tmp2[0]:
        tree[here] = tmp1[0]
        tree_index[here] = tmp1[1]
    elif tmp1[0] > tmp2[0]:
        tree[here] = tmp2[0]
        tree_index[here] = tmp2[1]
    else:
        if tmp1[1] < tmp2[1]:
            tree[here] = tmp1[0]
            tree_index[here] = tmp1[1]
        else:
            tree[here] = tmp2[0]
            tree_index[here] = tmp2[1]
    return [tree[here], tree_index[here]]


def update(start, end, here, index, value):
    if end < index or index < start:
        # 자식 노드랑 비교해서 부모 노드로 옮겨줘야 하는 작업 필요.
        return [tree[here], tree_index[here]]
    if index <= start and end <= index:
        tree[here] = value
        return [tree[here], tree_index[here]]
    mid = (start + end) // 2
    tmp1 = update(start, mid, here * 2, index, value)
    tmp2 = update(mid + 1, end, here * 2 + 1, index, value)
    if tmp1[0] < tmp2[0]:
        tree[here] = tmp1[0]
        tree_index[here] = tmp1[1]
    elif tmp1[0] > tmp2[0]:
        tree[here] = tmp2[0]
        tree_index[here] = tmp2[1]
    else:
        if tmp1[1] < tmp2[1]:
            tree[here] = tmp1[0]
            tree_index[here] = tmp1[1]
        else:
            tree[here] = tmp2[0]
            tree_index[here] = tmp2[1]
    return [tree[here], tree_index[here]]


def query(start, end, here, left, right):
    if left > end or right < start:
        # 필요 없는 노드 쪽은 대충 반환.
        return [1234567890, -1]
    if left <= start and end <= right:
        return [tree[here], tree_index[here]]
    mid = (start + end) // 2
    tmp1 = query(start, mid, here * 2 , left, right)
    tmp2 = query(mid + 1, end, here * 2 + 1, left, right)
    if tmp1[0] < tmp2[0]:
        return tmp1
    elif tmp1[0] > tmp2[0]:
        return tmp2
    else:
        if tmp1[1] < tmp2[1]:
            return tmp1
        else:
            return tmp2

# 값, 인덱스 트리 셋팅.
init(0, N - 1, 1)

M = int(input())
for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        update(0, N - 1, 1, cmd[1] - 1, cmd[2])
    else:
        print(query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)[1] + 1)
