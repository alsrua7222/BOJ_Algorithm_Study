class Tree:
    def __init__(self):
        self.dict1 = dict()
    def insert(self, root, left, right):
        self.dict1[root] = [left, right]
    def preorder(self, start):
        print(start, end="")
        if self.dict1[start][0] != '.':
            self.preorder(self.dict1[start][0])
        if self.dict1[start][1] != '.':
            self.preorder(self.dict1[start][1])
        return
    def inorder(self, start):
        if self.dict1[start][0] != '.':
            self.inorder(self.dict1[start][0])
        print(start, end="")
        if self.dict1[start][1] != '.':
            self.inorder(self.dict1[start][1])
        return
    def postorder(self, start):
        if self.dict1[start][0] != '.':
            self.postorder(self.dict1[start][0])
        if self.dict1[start][1] != '.':
            self.postorder(self.dict1[start][1])
        print(start, end="")
        return
N = int(input())
tree = Tree()
for _ in range(N):
    cmd = input().split()
    tree.insert(cmd[0], cmd[1], cmd[2])

tree.preorder('A')
print()
tree.inorder('A')
print()
tree.postorder('A')
