# 와이파이
https://www.acmicpc.net/problem/23826
## 해결 과정
### 0. 정리
말이 복잡하게 설명해놔서 어렵게 느끼지. 알고보면 너무 쉬운 문제임.    
먼저 공용 와이파이 값을 X, Y, E 라고 함.   
핫스팟 와이파이 위치(x, y, e) 쪽으로 송신할 때,    
E - max(0, (|X - x| + |Y - y|)) 하면 된다.    
그리고 공용 와이파이가 전송한 값에 해당 핫스팟 위치 제외한 나머지 다른 핫스팟 전파 간섭의 합을 빼야 되니까   
다른 핫스팟 위치를 x2, y2, e2 라고 하자.    
answer -= max(0, e - (|x - x2| + |y - y2|)) 하면 된다.    
이걸 모든 위치에 대해서 다 계산해야 하니, 브루트 포스 부류 문제다.   
나만 당했던 함정 하나 있었는데, 공용 와이파이 수신받는 쪽도 전파 간섭에 포함한다 ㅋㅋㅋ      
### 1. 입력받으면서 계산 처리.
```python
N = int(input())
arr = []
answer = []
X, Y, E = map(int, input().split())
for i in range(N):
    arr.append(list(map(int, input().split())))
    answer.append(max(0, E - (abs(arr[i][0] - X) + abs(arr[i][1] - Y))) - arr[i][2])
    for j in range(i):
        answer[j] -= max(0, arr[i][2] - (abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])))
        answer[i] -= max(0, arr[j][2] - (abs(arr[j][0] - arr[i][0]) + abs(arr[j][1] - arr[i][1])))
```
먼저 공용 와이파이 값을 넣고 바로 수신된 와이파이 값을 뺀다. 같은 자리에서 발산하니까 E - 0 = E 인 셈이다.    
### 2. 모든 방에서 가장 큰 값을 출력하기.
단, 전부 0으로 되어 있다면 안된다.   
```python
MAX = 0
for v in answer:
    if v < 0:
        print("IMPOSSIBLE")
        exit(0)
    elif v > MAX:
        MAX = v
print(MAX if MAX != 0 else "IMPOSSIBLE")
```
