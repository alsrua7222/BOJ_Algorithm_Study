import sys
input = sys.stdin.readline

def solve(layout):
    for i in range(8):
        R = 0
        for j in range(8):
            if layout[i][j] == 'R':
                R += 1

        if R == 8:
            return "R"
    
    for i in range(8):
        B = 0
        for j in range(8):
            if layout[j][i] == 'B':
                B += 1
                
        if B == 8:
            return "B"

for tc in range(int(input())):
    input()
    layout = [input().rstrip() for i in range(8)]
    print(solve(layout))