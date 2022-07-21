def checkRow(grid, row):
    check = set()
    for col in range(9):
        if grid[row][col] in check:
            return False
        check.add(grid[row][col])
    return True
def checkCol(grid, col):
    check = set()
    for row in range(9):
        if grid[row][col] in check:
            return False
        check.add(grid[row][col])
    return True
def check3x3(grid, row, col):
    check = set()
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if grid[r][c] in check:
                return False
            check.add(grid[r][c])
    return True
def solve(grid):
    for row in range(9):
        if not checkRow(grid, row):
            return False
    
    for col in range(9):
        if not checkCol(grid, col):
            return False
    
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not check3x3(grid, row, col):
                return False
    return True
for tc in range(1, int(input()) + 1):
    if tc != 1:
        input()
    grid = [list(map(int, input().split())) for _ in range(9)]
    print(f"Case {tc}:", end=" ")
    print("CORRECT" if solve(grid) else "INCORRECT")