N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

check = [True] * 1000
for num in range(123, 1000):
    string = str(num)
    if '0' in string or string[0] == string[1] or string[1] == string[2] or string[0] == string[2]:
        check[num] = False
        continue

    for i in range(N):
        string2 = str(arr[i][0])
        strike = 0
        ball = 0

        if string[0] == string2[0]:
            strike += 1
        if string[1] == string2[1]:
            strike += 1
        if string[2] == string2[2]:
            strike += 1

        if string[0] == string2[1] or string[0] == string2[2]:
            ball += 1
        if string[1] == string2[0] or string[1] == string2[2]:
            ball += 1
        if string[2] == string2[0] or string[2] == string2[1]:
            ball += 1
        
        if strike != arr[i][1] or ball != arr[i][2]:
            check[num] = False

answer = sum(check[123:])
print(answer)