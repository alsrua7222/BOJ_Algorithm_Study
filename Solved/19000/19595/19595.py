MAX = 100000
primes = [True] * (MAX + 1)

for i in range(2, MAX + 1):
    if primes[i]:
        for j in range(i + i, MAX + 1, i):
            primes[j] = False

arr = []
for i in range(2, MAX + 1):
    if primes[i]:
        arr.append(i)

wins = [0] * (MAX + 1)
for i in range(MAX + 1):
    if wins[i]:
        continue
    for j in range(len(arr)):
        if i + arr[j] > MAX:
            break
        wins[i + arr[j]] = 1