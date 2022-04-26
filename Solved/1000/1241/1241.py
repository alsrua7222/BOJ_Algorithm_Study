import sys
input = sys.stdin.readline

N = int(input())
inputs = []
arr = []

for _ in range(N):
    # 동적 배열 할당
    num = int(input())
    inputs.append(num)

    while len(arr) < num + 1:
        arr.append(0)

    arr[num] += 1

# 약수 구하기
result = ""
for i in range(N):
    answer = 0
    for j in range(1, int(inputs[i]**.5) + 1):
        if inputs[i] % j == 0:
            if inputs[i] // j != j:
                answer += arr[j] + arr[inputs[i] // j]
            else:
                answer += arr[j]
    result += (str(answer - 1) + "\n")
print(result)
