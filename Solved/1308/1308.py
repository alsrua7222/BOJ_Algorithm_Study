# 풀이 과정
# https://blog.naver.com/alsrua7222/222679224387

start = list(map(int, input().split()))
D_Day = list(map(int, input().split()))
mons = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def Is4(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    return 0

def getDays(y, m, d):
    ret = 0
    for i in range(y):
        ret += 365 + Is4(i)
    for i in range(m - 1):
        if i == 1:
            ret += Is4(y)
        ret += mons[i]
    return ret + d

if D_Day[0] - start[0] >= 1000:
    if (D_Day[0] - start[0] > 1000) or (getDays(0, D_Day[1], D_Day[2]) - getDays(0, start[1], start[2]) >= 0):
        print("gg")
        exit(0)

print(f"D-{getDays(D_Day[0], D_Day[1], D_Day[2]) - getDays(start[0], start[1], start[2])}")
