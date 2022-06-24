arr = []
A, B = map(int, input().split())
C, D = map(int, input().split())
arr = [[0, A / C + B / D]]
arr.append([1, C / D + A / B])
arr.append([2, D / B + C / A])
arr.append([3, B / A + D / C])
arr.sort(key=lambda x: -x[1])
print(arr[0][0])
