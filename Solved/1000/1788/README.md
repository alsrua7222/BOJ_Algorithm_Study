# 피보나치 수의 확장
https://www.acmicpc.net/problem/1788
## 해결 과정
### 0. 11444번 문제 풀이 과정이랑 매우 비슷하다.
### 1. 단, 이 문제에서는 음수로 확장한 개념이기 때문에 점화식을 찾아본다.
### 2. 너무 간단하다. N이 음수이고, |N|이 짝수라면 Fibo(N)에 -1 곱한거랑 같다.
### 3. 홀수는 Fibo(N)를 호출하면 된다.
### 4. 결과값은 절댓값으로 호출하고 나머지 1e9으로 나눠서 출력한다는 것을 명심하자.
