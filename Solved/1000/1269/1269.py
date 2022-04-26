# 풀이 과정
# https://blog.naver.com/alsrua7222/222658769362

input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_b = set(A) - set(B)
b_a = set(B) - set(A)
print(len(a_b | b_a))