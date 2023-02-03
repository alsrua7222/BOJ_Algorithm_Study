# [인증평가(5차) 기출] 업무 처리
# https://softeer.ai/practice/info.do?idx=1&eid=1256

import sys
input = sys.stdin.readline

from collections import deque
H, K, R = map(int, input().split())
leap_nodes = [deque(map(int, input().split())) for _ in range(2 ** H)]
class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.root = deque()
class Tree:
    def __init__(self, height) -> None:
        self.tree = [Node() for _ in range(2 ** height * 2)]
        self.tree[0] = 0 # Sum
        self.init_tree(0, 2 ** height - 1, 1)
        return

    def init_tree(self, start, end, here):
        if start == end:
            self.tree[here].root = leap_nodes[start]
            return self.tree[here]
        mid = (start + end) // 2
        self.tree[here].left = self.init_tree(start, mid, here * 2)
        self.tree[here].right = self.init_tree(mid + 1, end, here * 2 + 1)
        return self.tree[here]
    
    def update(self, start, end, here, parent, IsOdd):
        if start == end:
            if here % 2 == IsOdd and self.tree[here].root:
                self.tree[parent].root.append(self.tree[here].root.popleft())
            return
        if parent == 0:
            if self.tree[here].root:
                self.tree[parent] += self.tree[here].root.popleft()
        if here % 2 == IsOdd:
            if self.tree[here].root:
                value = self.tree[here].root.popleft()
                if parent != 0:
                    self.tree[parent].root.append(value)
            
        mid = (start + end) // 2
        self.update(start, mid, here * 2, here, IsOdd)
        self.update(mid + 1, end, here * 2 + 1, here, IsOdd)
        return

tree = Tree(H)
for today in range(1, R + 1):
    tree.update(0, 2 ** H - 1, 1, 0, today % 2)
print(tree.tree[0])