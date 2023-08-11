from collections import deque
def solve():
    N = int(input())
    arr = []
    for _ in range(N):
        x, y = map(int, input().split())
        arr.append((x, y))

    arr.sort(key=lambda x: x[0])

    queue = deque()
    area = 0
    for x, y in arr:
        if not queue:
            queue.append((x, y))
            continue
        
        if queue[-1][1] >= y:
            queue.append((x, y))
            continue
        
        while queue:
            sx, sy = queue[-1]
            if sy < y:
                queue.pop()
                
                if queue:
                    if queue[-1][1] < y:
                        continue
                    if queue[-1][1] > y:
                        queue.append((sx, y))
                    break
                    
            if not queue:
                area += (x - sx) * sy
            
        queue.append((x, y))
    
    while queue:
        sx, sy = queue.popleft()
        if queue:
            if queue[0][1] != sy:
                area += sy
                if queue[0][0] != sx + 1:
                    queue.appendleft((sx + 1, queue[0][1]))
            else:
                area += (queue[0][0] - sx) * sy
        else:
            area += sy
        
    return area

print(solve())