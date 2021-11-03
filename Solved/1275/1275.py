import sys, math
input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
h = math.ceil(math.log2(N))
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

for i in range(N):
	update(0, N - 1, 1, i, arr[i])

def query(start, end, here, left, right):
	if right < start or end < left:
		return 0
	if left <= start and end <= right:
		return tree[here]
	mid = (start + end) // 2
	return query(start, mid, here * 2, left, right) + query(mid + 1, end, here * 2 + 1, left, right)

for _ in range(Q):
	x, y, a, b = map(int, input().split())
	if x > y:
		x, y = y, x
	print(query(0, N - 1, 1, x - 1, y - 1))
	diff = b - arr[a - 1];
	arr[a - 1] = b
	update(0, N - 1, 1, a - 1, diff)
