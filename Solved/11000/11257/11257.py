for _ in range(int(input())):
    query = list(map(int, input().split()))
    answer = "FAIL"
    if sum(query[1:]) >= 55:
        if query[1] >= 35 * 0.3 and query[2] >= 25 * 0.3 and query[3] >= 40 * 0.3:
            answer = "PASS"
    print(query[0], sum(query[1:]), answer)