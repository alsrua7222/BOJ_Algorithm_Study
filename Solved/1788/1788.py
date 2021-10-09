import copy
C = 10**9

N = int(input())
op = 1
if N < 0:
    N = -N
    if N & 1 == 0:
        op = -op

def matrix_mul(a, b):
    result = [[0 for row in range(2)] for col in range(2)]
    result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % C
    result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % C
    result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % C
    result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % C
    return result

zero = [[1, 0], [0, 1]]
pibo = [[1, 1], [1, 0]]

i = 0
zero_tmp = copy.deepcopy(zero)
pibo_tmp = copy.deepcopy(pibo)

while 2 ** i <= N:
    if N & (1 << i) != 0:
        zero_tmp = matrix_mul(zero_tmp, pibo_tmp)
    i += 1
    pibo_tmp = matrix_mul(pibo_tmp, pibo_tmp)

tmp = op * (zero_tmp[1][0] % C)
if tmp > 0:
    print(1)
elif tmp == 0:
    print(0)
else:
    print(-1)
print(abs(tmp))
