n, d = input().split()
n = int(n)

if len(d) > n:
    print("No solution")
else:
    answer = d
    for i in range(n - len(d)):
        answer += "0"
    print(answer)