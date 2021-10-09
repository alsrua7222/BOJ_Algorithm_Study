import copy
C = 10**9 + 7
def matrix_mul(a, b):
    result = [[0 for row in range(2)] for col in range(2)]
    result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % C
    result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % C
    result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % C
    result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % C
    return result

N = int(input())
binN = bin(N)[2:]
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

print(zero_tmp[1][0] % C)
