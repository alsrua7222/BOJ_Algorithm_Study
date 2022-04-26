import copy


N = int(input())

def getPibo(N):
    def matrix_mul(a, b):
        result = [[0 for row in range(2)] for col in range(2)]
        result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0])
        result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1])
        result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0])
        result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1])
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

    return zero_tmp[1][0]
print(getPibo(N))
