vis =  [False] * 31
for _ in range(28):
    vis[int(input())] = True
for i in range(1, 31):
    if not vis[i]:
        print(i)
