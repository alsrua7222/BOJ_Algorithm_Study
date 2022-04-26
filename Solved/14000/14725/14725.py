# 풀이 과정
# https://blog.naver.com/alsrua7222/222628117642

import sys
from collections import defaultdict
input = sys.stdin.readline

class Ant:
    def __init__(self):
        self.children = defaultdict(Ant)

    def insert(self, arr, cur):
        if cur == len(arr):
            return

        self.children[arr[cur]].insert(arr, cur + 1)
        return

    def search(self, level):
        if not self.children:
            return

        for key, values in sorted(self.children.items()):
            print("--" * level, key, sep="")
            values.search(level + 1)
        return

N = int(input())
root = Ant()
for _ in range(N):
    sub = input().split()
    root.insert(sub[1:], 0)

root.search(0)