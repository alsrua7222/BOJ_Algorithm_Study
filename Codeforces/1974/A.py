import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    answer = 0
    
    while x > 0 or y > 0:
        if y >= 2:
            y -= 2
            x -= 7
            answer += 1
        elif y == 1:
            y -= 1
            x -= 11
            answer += 1
        else:
            x -= 15
            answer += 1
    print(answer)
        