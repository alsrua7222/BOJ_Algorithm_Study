# 풀이 과정
# https://blog.naver.com/alsrua7222/222678304711

arr = []
A, B = map(int, input().split())
cnt = 0
cur = 1
while len(arr) <= B:
    arr.append(cur)
    cnt += 1
    if cnt == cur:
        cnt = 0
        cur += 1
print(sum(arr[A - 1:B]))