for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)

    success = True

    if n % 2 == 0:
        for i in range(0, n - 1, 2):
            if sorted_a[i] == a[i] and sorted_a[i + 1] == a[i + 1]:
                success = True
            else:
                success = False
                break
    elif n != 1:
        if sorted_a[-1] != a[-1]:
            success = False
        else:
            for i in range(n - 1, 2):
                if sorted_a[i] == a[i + 1] and sorted_a[i + 1] == a[i]:
                    success = True
                else:
                    success = False
                    break

    if n == 1:
        success = True
    
    print("YES" if success else "NO")