from collections import Counter
def solution(a, b, c, d):
    answer = 0
    cnt = Counter([a, b, c, d]).most_common()
    l = len(cnt)
    if l == 1:
        return 1111 * cnt[0][0]
    
    if l == 2:
        p, q = cnt[0][0], cnt[1][0]
        if cnt[0][1] == 2:
            return (p + q) * abs(q - p)
        else:
            return (10 * p + q) ** 2
    
    if l == 3:
        p, q, r = cnt[0][0], cnt[1][0], cnt[2][0]
        return q * r
    
    return min([a, b, c, d])