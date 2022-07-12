import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    grid = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    
    def check(x, y, grid, visited):
        nxy = [(x, y), (y, n - 1 - x), (n - 1 - x, n - 1 - y), (n - 1 - y, x)]
        for nx, ny in nxy:
            visited[nx][ny] = True

        same = True
        target = grid[x][y]
        cnt_0, cnt_1 = 0, 0
        for nx, ny in nxy:
            if grid[nx][ny] == 1:
                cnt_1 += 1
            else:
                cnt_0 += 1

            if target != grid[nx][ny]:
                same = False
        
        if same:
            return 0
        
        if cnt_1 == 3 or cnt_0 == 3:
            return 1
        else:
            return 2

    def makeSameGrid(grid):
        ret = 0
        visited = [[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if visited[x][y]:
                    continue
                ret += check(x, y, grid, visited)
        return ret
    
    print(makeSameGrid(grid))