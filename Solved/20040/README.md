# 사이클 게임
https://www.acmicpc.net/problem/20040
## 해결 과정
### 0. 그래프를 떠올려보면서 충분히 생각을 가진다.
### 1. 사이클을 발생하려면 정점 개수가 3개 이상 이고, 서로 직/간접적 관계가 있어야 한다.
### 2. 그래서 분리 집합임을 알 수 있었다.
### 3. N의 크기가 500,000이고, 쿼리 M의 길이가 1,000,000 이므로 이는 메모리 구조 하나로 응용하면서 풀어야 한다는 것을 알았다.
### 4. 유니온 파인드로 푼다.
번호 값대로 이어지기 때문에 parents 배열에 자기 번호를 넣을 수 있도록 한다.   
```
for i in range(N + 1): parents[i] = i
```

```
def find(x):
    if parents[x] == x:
        return x
    else:
        p = find(parents[x])
        parents[x] = p
        return p
```

```
def union(x, y):
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
```
번호 값대로 이어지므로 이에 맞게 구현한다.    

```
success = False

for i in range(M):
    n, m = map(int, input().split())
    if success:
        continue
    a = find(n)
    b = find(m)
    if a == b:
        print(i + 1)
        success = True
    union(a, b)
    
if not success:
    print(0)
```
success 선언한 이유는 최초로 사이클을 발견하면 더 이상 아무 동작을 하지마라고 하는 것이다.   
