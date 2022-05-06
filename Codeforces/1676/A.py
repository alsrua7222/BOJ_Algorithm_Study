for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    left = 0
    right = n - 1

    while left < right:
        if a[left] >= 0 and a[right] < 0:
            a[left] *= -1
            a[right] *= -1
            left += 1
            right -= 1

        if a[left] < 0:
            left += 1

        if a[right] >= 0:
            right -= 1
    
    success = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            success = False
            break
    print("YES" if success else "NO")