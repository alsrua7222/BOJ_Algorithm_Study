import sys, copy
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    grid_sort = [sorted(grid[i]) for i in range(n)]
    
    success = True
    collect = []
    cnt2 = 0
    for i in range(n):
        cnt = 0
        tmp = []
        for j in range(m):
            if grid[i][j] != grid_sort[i][j]:
                cnt += 1
                tmp.append(j)

        if cnt > 2 or cnt == 1:
            success = False
            break
        elif cnt == 0:
            cnt2 += 1

        collect.append(tmp)
    
    if cnt2 == n:
        print(1, 1)
        continue

    if not success:
        print(-1)
        continue
    
    first_xy = []
    for i in range(n):
        if len(collect[i]) == 0:
            continue
        elif not first_xy:
            first_xy = [collect[i][0], collect[i][1]]
        else:
            if first_xy[0] != collect[i][0] or first_xy[1] != collect[i][1]:
                success = False
                break

    if not success:
        print(-1)
    else:
        new_grid = copy.deepcopy(grid)
        for i in range(n):
            new_grid[i][first_xy[0]], new_grid[i][first_xy[1]] = new_grid[i][first_xy[1]], new_grid[i][first_xy[0]]

        new_grid_sort = [sorted(new_grid[i]) for i in range(n)]
        for i in range(n):
            for j in range(m):
                if new_grid[i][j] != new_grid_sort[i][j]:
                    success = False
                    break
            if not success:
                break
        
        if not success:
            print(-1)
        else:
            print(first_xy[0] + 1, first_xy[1] + 1)