import math, sys
input = sys.stdin.readline
try:
    while True:
        N, M = map(int, input().split())
        arr = list(map(int, input().split()))
        for i in range(len(arr)):
            if arr[i] != 0:
                if arr[i] > 0:
                    arr[i] = 1
                else:
                    arr[i] = -1
        tree = [0] * (1 << (math.ceil(math.log2(N)) + 1))
        def init(start, end, here):
            if start == end:
                tree[here] = arr[start]
                return tree[here]
            mid = (start + end) // 2
            tree[here] = init(start, mid, here * 2) * init(mid + 1, end, here * 2 + 1)
            return tree[here]
        def update(start, end, here, index, value):
            if index < start or end < index:
                return tree[here]
            if start == end:
                tree[here] = value
                return tree[here]

            mid = (start + end) // 2
            tree[here] = update(start, mid, here * 2, index, value) * update(mid + 1, end, here * 2 + 1, index, value)
            return tree[here]

        def query(start, end, here, left, right):
            if right < start or end < left:
                return 1
            if left <= start and end <= right:
                return tree[here]
            mid = (start + end) // 2
            return query(start, mid, here * 2, left, right) * query(mid + 1, end, here * 2 + 1, left, right)

        init(0, N - 1, 1)
        answer = ""
        for _ in range(M):
            cmd = list(input().split())
            cmd[1:] = map(int, cmd[1:])
            if cmd[0] == 'C':
                if cmd[2] > 0:
                    cmd[2] = 1
                elif cmd[2] < 0:
                    cmd[2] = -1
                update(0, N - 1, 1, cmd[1] - 1, cmd[2])
            else:
                tmp = query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)
                answer += "+" if tmp > 0 else '0' if tmp == 0 else '-'
        print(answer)
except:
    pass
