import sys
input = sys.stdin.readline
for _ in range(int(input())):
    string = list(input().rstrip())
    
    answer = 0
    index = 0
    while index < len(string):
        set1 = set()
        cnt = 0
        while index < len(string):
            if string[index] not in set1:
                if cnt < 3:
                    set1.add(string[index])
                else:
                    break
                cnt += 1
            index += 1
        answer += 1
    print(answer)
    