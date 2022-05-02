dict1 = {}
cnt = 1
for i in range(26):
    for j in range(26):
        if i == j:
            continue
        dict1[chr(i + ord('a')) + chr(j + ord('a'))] = cnt
        cnt += 1

for _ in range(int(input())):
    print(dict1[input()])