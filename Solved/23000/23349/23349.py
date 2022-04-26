N = int(input())
name = set()
place = dict()

for _ in range(N):
    n, p, start, end = input().split()
    start, end = int(start), int(end)

    if n not in name:
        name.add(n)

        if p not in place:
            place[p] = [[start, end]]
        else:
            place[p].append([start, end])

def getMax(p):
    # 오름차순으로 정렬.
    s, e = [], []
    for v1, v2 in p:
        s.append(v1)
        e.append(v2)
    s.sort(), e.sort()
    # 최대개수, 최대개수에서 스타트 지점, 최대개수에서 엔드 지점
    MAX = [0, 0, 0]
    cnt, start, end = 0, 0, 0

    # 스타트 지점 정리.
    while start != len(p):
        if e[end] <= s[start]:
            # 해당 구간의 종료 시점이 스타트 지점보다 같거나 작다면 종료 카운팅.
            cnt -= 1
            end += 1
        elif s[start] < e[end]:
            # 해당 구간의 스타트 지점이 엔드 지점보다 작다면 스타트 카운팅.
            cnt += 1
            # MAX 갱신
            if MAX[0] < cnt:
                MAX = [cnt, s[start], e[end]]
            start += 1

    return MAX

answer = []
for k in place.keys():
    answer.append([k] + getMax(place[k]))
answer.sort(key=lambda x: (-x[1], x[0]))
# print(answer)
print(answer[0][0], answer[0][2], answer[0][3])
