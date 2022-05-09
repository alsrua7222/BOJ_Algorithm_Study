strings = input().split()
n = int(input())
count = list(map(int, input().split()))

if len(strings) - 1 > n:
    print(-1)
    exit(0)

answer = ""
success = True
for string in strings:
    for i in range(len(string)):
        if i >= 1 and string[i] == string[i - 1]:
            continue
        if count[ord(string[i].upper()) - ord('A')] > 0:
            count[ord(string[i].upper()) - ord('A')] -= 1
        else:
            success = False
            break
    if success:
        answer += string[0].upper()
    else:
        break

if success:
    tmp = answer.lower()
    for i in range(len(tmp)):
        if i >= 1 and tmp[i] == tmp[i - 1]:
            continue
        if count[ord(tmp[i].upper()) - ord('A')] > 0:
            count[ord(tmp[i].upper()) - ord('A')] -= 1
        else:
            success = False
            break
    if success:
        print(answer)
        exit(0)
print(-1)