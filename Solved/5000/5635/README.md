# 생일
https://www.acmicpc.net/problem/5635
## 해결 과정
### 0. 나이가 많은 기준 - 생년월일이 가장 작아야 한다. 즉, 1년 1월 1일이 제일 나이가 많다.
### 1. 나이가 적은 기준 - 생년월일이 가장 커야 한다. 즉, 999년 12월 31일이 제일 나이가 적다.
### 2. 이 문제 같은 경우, 생년월일이 같지 않게 주어진다.
### 3. 아래 조건을 만족하면서 오름차순으로 정렬한다.
```c++
typedef struct info {
	string s;
	int d, m, y;
}info;
```
입력 타입에 맞게 구조체를 선언해준다.   
```c++
bool compare(const info& a, const info& b) {
	if (a.y < b.y) return true;
	else if (a.y == b.y) {
		if (a.m < b.m) return true;
		else if (a.m == b.m) {
			if (a.d < b.d) return true;
		}
	}
	return false;
}
```
a에 들어온 비교대상1과 b에 들어온 비교대상2 라고 하면,     
a의 생년이 b의 생년보다 작으면 오름차순 정렬을 적용시켜야 하므로 true 반환.    
만약에 생년이 같다면 a의 월이 b의 월보다 작으면 오름차순 정렬으로 true 반환.   
만약에 월까지 같다면 a의 일이 b의 일보다 작으면 오름차순 정렬으로 true 반환한다.   
그 외는 정렬하지 않는다.    
### 4. 나이가 많은 것은 구조 상에서 맨 앞자리에 있고, 나이가 적은 것은 구조 상에서 맨 뒤자리에 있다.
### 출력한다.
