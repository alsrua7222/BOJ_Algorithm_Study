import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()

    answer = 0
    for i in range(0, n, 2):
        if s[i] != s[i + 1]:
            answer += 1
    
    print(answer)