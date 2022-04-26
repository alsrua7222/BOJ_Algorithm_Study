# 단축키 지정
https://www.acmicpc.net/problem/1283
## 해결 과정
### 0. 처음에는 단어 분리하고 각 단어의 첫 글자가 사용되었는지 체크하고 셋팅한다.
### 1. 체크가 안됐다면 처음부터 끝까지 탐색하면서 각 원소가 사용되었는지 체크하고 셋팅한다.
### 2. 최종 결과물은 아래와 같다. 역시 쉬웠다.
```python
N = int(input())
answer = ""
set1 = set()
for _ in range(N):
    tmp = list(input().split())
    success = False
    idx = -1
    for v in tmp:
        idx += 1
        if v[0] not in set1:
            set1.update([v[0].upper(), v[0].lower()])
            success = True
            break
    if success:
        for i in range(len(tmp)):
            if idx == i:
                answer += f"[{tmp[i][0]}]{tmp[i][1:]}"
            else:
                answer += tmp[i]
            answer += ' '
        answer += "\n"
        continue

    for v in tmp:
        for v2 in v:
            if not success and v2 not in set1:
                answer += f"[{v2}]"
                set1.update([v2.upper(), v2.lower()])
                success = True
            else:
                answer += v2
        answer += ' '
    answer += "\n"
print(answer)
```
