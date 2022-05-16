import sys; input = sys.stdin.readline
from collections import defaultdict
N, M = map(int, input().split())
dict1 = defaultdict(list)
for i in range(N):
    tmp = input().rstrip()
    dict1[tmp[0]].append(tmp)

cnt_max = [0] * 26
cnt = [0] * 26
for i in range(26):
    cnt_max[ord(chr(i + ord('a'))) - ord('a')] = len(dict1[chr(i + ord('a'))])
    dict1[chr(i + ord('a'))].sort()

for i in range(M):
    ch = input().rstrip()
    ch_idx = ord(ch) - ord('a')
    print(dict1[ch][cnt[ch_idx]])
    cnt[ch_idx] = (cnt[ch_idx] + 1) % cnt_max[ch_idx]