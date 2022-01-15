# 풀이 과정
# https://blog.naver.com/alsrua7222/222622774862

N, d = map(int, input().split())

def convertD(n):
    result = ""
    while n > 0:
        n, mod = divmod(n, d)
        result += str(mod)
    return result[::-1]

def convertN(D):
    result = 0
    for i in range(len(D)):
        result += int(D[-(i + 1)]) * (d ** i)
    return result


conv = convertD(N)
if len(conv) > d:
    print(-1)
    exit(0)

conv = int(conv)

def backtracking(cur, used: list, acc, root = True):
    global answer
    if cur == d:
        if acc > conv:
            answer = acc
            return True
        else:
            return False

    for i in range(d):

        if root and i == 0:
            continue
        if i not in used:
            if backtracking(cur + 1, used + [i], acc * 10 + i, False):
                return True

    return False

answer = -1
if backtracking(0, [], 0):
    print(convertN(str(answer)))
else:
    print(answer)
