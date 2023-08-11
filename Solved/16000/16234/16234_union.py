import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
population = []
for i in range(n):
    population.append(list(map(int, input().split())))

def find(x):
    global root
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x,y):
    global root
    x, y = find(x), find(y)
    x, y = min(x, y), max(x, y)
    root[y] = x
    return

def move_population():
    global root
    pop_dict = {}
    index_dict = {}
    for i in range(n):
        for j in range(n):
            index = (i * n + j) + 1
            if root[index] in pop_dict:
                pop_dict[root[index]].append(population[i][j])
                index_dict[root[index]].append((i, j))
            else:
                pop_dict[root[index]] = [population[i][j]]
                index_dict[root[index]] = [(i, j)]

    for key, value in pop_dict.items():
        if len(value) != 1:
            aver = sum(value) // len(value)
            for x, y in index_dict[key]:
                population[x][y] = aver

count = 0
while(True):
    root = list(range(0, n ** 2 + 2))
    is_open = False
    for row in range(n):
        for col in range(n):
            index = row * n + col + 1
            
            if row > 0:
                up_idx = index - n
                if l <= abs(population[row][col] - population[row - 1][col]) <= r:
                    union(index, up_idx)
                    is_open = True

            if row < n - 1:
                down_idx = index + n
                if l <= abs(population[row][col] - population[row + 1][col]) <= r:
                    union(index, down_idx)
                    is_open = True
            
            if col < n - 1:
                right_idx = index + 1
                if l <= abs(population[row][col] - population[row][col + 1]) <= r:
                    union(index, right_idx)
                    is_open = True
            
            if col > 0:
                left_idx = index - 1
                if l <= abs(population[row][col] - population[row][col - 1]) <= r:
                    union(index, left_idx)
                    is_open = True

    if is_open:
        move_population()
        count += 1
    else:
        break
print(count)