# Watering the Fields
https://www.acmicpc.net/problem/10021
## 해결 과정
### 0. 영어 원문 요약은 아래와 같다.
1. 농부 존은 필드 사이에 워터스프링 파이프라인을 몇개를(N) 설치하려고 한다.      
2. 하지만 농부 존은 구두쇠 정신이 있어서 최소한 비용으로 하고 싶었다.
3. 하지만 너무 싼 값이면 고장나기 때문에 필드 사이에 설치할 파이프라인을 최소한 설치 비용(C)을 설정해두려고 한다.
4. 모든 파이프라인에 각 연결하되, 조건에 맞게 설치하려고 한다.
### 1. MST 알고리즘, union find을 쓰면 된다.
### 2. 단, 설치 최소 비용 조건을 만족하면 설치하도록 한다.
### 3. 조건들을 이행했지만, 각 사이에 연결되어 있지 않으면 -1로 출력한다.