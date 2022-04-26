# 왕위 계승
https://www.acmicpc.net/problem/5021
## 해결 과정
### 0. 유토피아의 왕이 혈통 수치가 1라고하고 배우자가 왕의 혈통이 아닐 경우 0이고, 자식에게 물려줄 수 있는 왕의 혈통 수치는 (1 + 0) / 2 = 0.5이다.
### 1. 위와 같은 방식으로 계승을 전달된다.
### 2. 마치 재귀함수로 푸는 것으로 보인다. 후보자들 이름으로 스타트해서 부모의 이름을 또 다시 재귀적으로 돌게 하여 반환값을 이어 받는 것이다.
### 3. 후보자의 이름을 역추적으로 부모의 노드를 거슬러 올라가면서 혈통이 몇인지 따져보면 된다.
```python
def backTracking(name):
    if name not in Graph:
        return Blood[name]
    p1, p2 = Graph[name]
    Blood[name] = (backTracking(p1) + backTracking(p2)) / 2
    return Blood[name]
```
### 4. 출력단에 [0, ""]를 셋팅해두고 후보자의 혈통 수치가 answer[0] == 0 보다 크다면, answer = [후보자의 혈통 수치, 후보자의 이름]을 갱신한다.
### 5. 왜 위상정렬인지 잘 모르겠다.
