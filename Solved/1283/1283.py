N = int(input())
answer = ""
set1 = set()
for _ in range(N):
    tmp = list(input().split())
    success = False
    idx = -1
    for v in tmp:
        idx += 1
        if v[0] not in set1:
            set1.update([v[0].upper(), v[0].lower()])
            success = True
            break
    if success:
        for i in range(len(tmp)):
            if idx == i:
                answer += f"[{tmp[i][0]}]{tmp[i][1:]}"
            else:
                answer += tmp[i]
            answer += ' '
        answer += "\n"
        continue

    for v in tmp:
        for v2 in v:
            if not success and v2 not in set1:
                answer += f"[{v2}]"
                set1.update([v2.upper(), v2.lower()])
                success = True
            else:
                answer += v2
        answer += ' '
    answer += "\n"
print(answer)
