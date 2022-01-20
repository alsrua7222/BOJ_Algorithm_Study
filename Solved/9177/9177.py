# 풀이 과정
# https://blog.naver.com/alsrua7222/222626716278

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(dp, x, y, l1, l2, t):
    if x + y == len(t):
        return True

    if dp[x][y]:
        return False
    dp[x][y] = True

    if x < len(l1) and l1[x] == t[x + y]:
        if DFS(dp, x + 1, y, l1, l2, t):
            return True
    if y < len(l2) and l2[y] == t[x + y]:
        if DFS(dp, x, y + 1, l1, l2, t):
            return True

    return False
def IsAble(target, list1, list2):
    # 길이가 같아야 한다.
    if len(target) != len(list1) + len(list2):
        return False

    # 타겟에 새로운 문자가 있거나 더 많거나 더 적으면 안된다.
    target_dict = defaultdict(int)
    for v in target:
        target_dict[v] += 1
    for v in list1:
        if v in target_dict and target_dict[v] > 0:
            target_dict[v] -= 1
        else:
            return False
    for v in list2:
        if v in target_dict and target_dict[v] > 0:
            target_dict[v] -= 1
        else:
            return False

    # 이상이 없다면 참 반환.
    return True


for i in range(1, int(input()) + 1):
    l1, l2, t = input().split()
    if IsAble(t, l1, l2):
        dp = [[False for y in range(len(l2) + 1)] for x in range(len(l1) + 1)]
        print(f"Data set {i}: {'yes' if DFS(dp, 0, 0, l1, l2, t) else 'no'}")
    else:
        print(f"Data set {i}: no")
