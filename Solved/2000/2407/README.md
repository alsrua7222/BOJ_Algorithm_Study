# 조합
https://www.acmicpc.net/problem/2407
## 해결 과정
### 0. 파스칼 삼각형처럼 DP로 C(N, M) = C(N-1, M-1) + C(N-1, M) 이 식이 성립함을 이용한다.
### 1. 열의 수는 M, 행의 수는 N만큼 dp 2차원을 0으로 초기화한다.
### 2. C(1, 1) = C(2, 2) = C(3, 3) = C(3, 0) = C(N, 0) = C(N, N) = 1임을 알 수 있다.
이 말은 C(1, 1)에서 1개 중에서 1개로 선택되는 경우의 수가 1가지.   
C(16, 16)에서 16개 중에서 16개로 선택 되는 경우의 수가 1가지.    
C(14, 0)에서 14개 중에서 0개로 선택 되는 경우의 수가 1가지.    
C(14, 1)에서 14개 중에서 1개로 선택 되는 경우의 수가 14가지.   
이해됬나?   
### 3. 즉, 위의 점화식을 따면 M == 0 혹은 M == N이면 1임을 알 수 있다.
### 4. M 길이까지 이므로 반복문에서 N이 M보다 크면 반복 중단하도록 한다.
### 5. 3, 4번 문제 조건을 통과되면 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]를 적립시킨다.
### 6. 그렇게 해서 dp[N][M]를 불러오면 끝