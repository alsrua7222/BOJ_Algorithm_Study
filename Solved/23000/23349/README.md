# 졸업 사진
https://www.acmicpc.net/problem/23349
## 해결 과정
### 0. 처음 제출이라면 해시테이블에 등록한다.
### 1. 중복 제출이라면 아무것도 안한다.
### 2. 입력단에서 끝나면 각 해시값(장소값 = 키값)으로 겹친 수가 더 많은 구간을 찾는다.
### 3. 그리디하게 스타트 지점과 끝나는 지점을 각 오름차순 정렬을 한다.
### 4. cnt, start, end 변수로 제어를 한다.
```python
def getMax(p):
    # 오름차순으로 정렬.
    s, e = [], []
    for v1, v2 in p:
        s.append(v1)
        e.append(v2)
    s.sort(), e.sort()
    # 최대개수, 최대개수에서 스타트 지점, 최대개수에서 엔드 지점
    MAX = [0, 0, 0]
    cnt, start, end = 0, 0, 0

    # 스타트 지점 정리.
    while start != len(p):
        if e[end] <= s[start]:
            # 해당 구간의 종료 시점이 스타트 지점보다 같거나 작다면 종료 카운팅.
            cnt -= 1
            end += 1
        elif s[start] < e[end]:
            # 해당 구간의 스타트 지점이 엔드 지점보다 작다면 스타트 카운팅.
            cnt += 1
            # MAX 갱신
            if MAX[0] < cnt:
                MAX = [cnt, s[start], e[end]]
            start += 1

    return MAX
```
### 5. answer에 반환값을 적재시킨다.
```python
answer = []
for k in place.keys():
    answer.append([k] + getMax(place[k]))
```
### 6. 끝나면 조건에 따라 정렬한다.
```python
answer.sort(key=lambda x: (-x[1], x[0]))
```
겹친 횟수가 많으면서 이름 오름차순으로 정렬한다.
### 7. 만족하는 출력 형태는 answer의 1번째 인덱스에 있다.
```python
print(answer[0][0], answer[0][2], answer[0][3])
```
