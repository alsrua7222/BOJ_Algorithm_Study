def georageCantor(n):
    i = 1
    j = 1
    k = 1

    while k < n:
        j += 1
        k += 1
        if k == n:
            break
        while j > 1 and k < n:
            i += 1
            j -= 1
            k += 1
        if k == n:
            break
        i += 1
        k += 1

        if k == n:
            break

        while i > 1 and k < n:
            i -= 1
            j += 1
            k += 1
    print(f"TERM {n} IS {i}/{j}")
    return

try:
    while True:
        georageCantor(int(input()))
except Exception:
    pass
