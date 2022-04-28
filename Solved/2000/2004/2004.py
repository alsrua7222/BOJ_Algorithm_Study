N, M = map(int, input().split())
two = 0
five = 0
def count_number(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return count

fn = [count_number(N, 2), count_number(N, 5)]
fm = [count_number(M, 2), count_number(M, 5)]
fnm = [count_number(N-M, 2), count_number(N-M, 5)]

first = fn[0] - (fnm[0] + fm[0])
second = fn[1] - (fnm[1] + fm[1])
print(min(first, second))

