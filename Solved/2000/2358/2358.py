import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input()); x = defaultdict(int); y = defaultdict(int);
for _ in range(N):
    a, b = map(int, input().split())
    x[a] += 1
    y[b] += 1
print(sum([1 for v in x.values() if v >= 2]) + sum([1 for v in y.values() if v >= 2]))
