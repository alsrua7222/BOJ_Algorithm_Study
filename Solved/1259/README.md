# 팰린드롬수
https://www.acmicpc.net/problem/1259
## 해결 과정
### 0. 0번째 인덱스와 N번째 인덱스를 비교한다. 같으면 넘어가고 다르면 즉시 종료한다.
### 1. 1번째와 N - 1 번째를 비교한다. 위와 동일.
### 2. 앞과 뒤를 비교해주면 되기 때문에 길이가 홀수 일 경우 가운데 인덱스는 무시한다.
문자열의 길이를 2로 정수형 값으로 나올 수 있게 나눠준다.     
### 3. 