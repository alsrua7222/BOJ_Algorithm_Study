for _ in range(int(input())):
    s = int(input())

    nations = dict()

    for i in range(s):
        name, voting = input().split()
        x, y, rank = map(int, input().split())

        nation = [name, voting, x, y, rank]
        nations[name] = nation
    
    r = int(input())
    want_name = input()
    want_nation = nations[want_name]

    p_arr = []
    q_arr = []
    base_score = 0

    def getDistance(voting, a):
        return ((voting[2] - a[2]) ** 2 + (voting[3] - a[3]) ** 2) ** 0.5

    for key in nations.keys():
        if want_nation == nations[key]:
            continue

        tmp = [value for value in nations.values()]
        tmp.remove(nations[key])
        
        if nations[key][1] == 'p':
            for i in range(len(tmp)):
                for j in range(i + 1, len(tmp)):
                    if getDistance(nations[key], tmp[i]) > getDistance(nations[key], tmp[j]):
                        tmp[i], tmp[j] = tmp[j], tmp[i]
        else:
            for i in range(len(tmp)):
                for j in range(i + 1, len(tmp)):
                    if tmp[i][4] > tmp[j][4]:
                        tmp[i], tmp[j] = tmp[j], tmp[i]
        
        rank = r
        for v in tmp:
            if v[:5] == want_nation:
                break
            rank -= 1
        
        if nations[key][1] == 'p':
            p_arr.append(rank)
        else:
            q_arr.append(rank)
        
        base_score += max(0, rank)
    # print(base_score)
    p_arr.sort(reverse=True)

    min_points = max(0, 2 + r - s)

    changed = [0] * (s - 1)
    for c in range(s - 1):
        tot_p = 0
        tot_i = 0

        left = c + 1
        for p in p_arr:
            if p + left > min_points:
                need = min(left, r - p)
                tot_i += min(need, max(p + need, min_points))
                left -= need
        for q in q_arr:
            tot_p += max(0, min(q - min_points, c + 1))
        
        changed[c] = tot_i - tot_p
    
    changed.sort()

    best_improvement = max(0, changed[-1])
    print(base_score + best_improvement)