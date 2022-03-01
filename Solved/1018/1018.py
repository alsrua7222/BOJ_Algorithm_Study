# 풀이 과정
# https://blog.naver.com/alsrua7222/222661184259

paint = ["WBWBWBWB", "BWBWBWBW"]
N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

def get8x8points(x, y, _type):
    sign = _type
    let = 0
    for i in range(8):
        for j in range(8):
            if arr[x+i][y+j] != paint[sign][j]:
                let += 1
        sign ^= 1
    return let

answer = 987654321
for X in range(N - 8 + 1):
    for Y in range(M - 8 + 1):
        answer = min(answer, get8x8points(X, Y, 0), get8x8points(X, Y, 1))

print(answer)