import math, sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (1 << (math.ceil(math.log2(N)) + 1))

# 누적합을 해서 왼쪽 서브 트리와 오른쪽 서브 트리 값을 찾으려 하는 값과 비교하는 식으로 만들어야 할 듯.
def init(start, end, here):
    if start == end:
        tree[here] = arr[start]
        return tree[here]
    mid = (start + end) // 2
    tree[here] = init(start, mid, here * 2) + init(mid + 1, end, here * 2 + 1)
    return tree[here]

# 업데이트는 그냥 구간값 변경하는 논리랑 같음.
def update(start, end, here, index, diff):
    if index < start or end < index:
        return

    tree[here] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, here * 2, index, diff)
        update(mid + 1, end, here * 2 + 1, index, diff)
        return

def bin_searchForSegTree(find):
    # 루트 노드 위치, 구간 길이
    cur, left, right = 1, 1, N

    while left < right:
        # 그냥 이분 탐색 구현에 서브트리 비교하는 조건으로 바꾸면 됨.
        mid = (left + right) // 2

        if tree[cur * 2] < find: # 오른쪽
            # 찾으려는 값이 왼쪽 서브트리보다 크면 찾으려는 값에 왼쪽 서브 트리 값을 빼고 탐색.
            find -= tree[cur * 2]

            cur = cur * 2 + 1
            left = mid + 1
        else: # 왼쪽
            cur = cur * 2
            right = mid

    return left

init(0, N - 1, 1)

for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        update(0, N - 1, 1, cmd[1] - 1, cmd[2])
    else:
        print(bin_searchForSegTree(cmd[1]))
