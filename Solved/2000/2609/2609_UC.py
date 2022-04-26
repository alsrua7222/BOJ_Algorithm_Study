N, M = map(int, input().split())


def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def lcm(n, m):
    return (n * m) // gcd(n, m)


print(gcd(N, M))
print(lcm(N, M))
