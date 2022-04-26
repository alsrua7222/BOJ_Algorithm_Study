#include <iostream> // min, max, stdio
#include <algorithm> // sort
#include <vector> // default data struct
#include <cmath> // pow, sqrt, ceil, floor
#include <sstream> // for string
#include <string> // string methods
#include <queue> // queue, priority_queue
#include <deque> // deque
#include <utility> // pair
#include <cstring>
#include <unordered_map> // hash_map (<hash_map> lib is not used, cuz will be delete lib.)
#include <set> // sorted set
#include <map> // sorted map
#include <stack> // stack
using namespace std;
/*
* 풀이 과정
* https://blog.naver.com/alsrua7222/222601478521
*/
int N;
vector<int> arr, tree;
int init(int start, int end, int here) {
	if (start == end) {
		return tree[here] = 1;
	}
	int mid = (start + end) / 2;
	return tree[here] = init(start, mid, here * 2) + init(mid + 1, end, here * 2 + 1);
}

int update(int start, int end, int here, int index) {
	if (start > index || index > end) return tree[here];

	if (start == end) return tree[here] = 0;
	int mid = (start + end) / 2;
	return tree[here] = update(start, mid, here * 2, index) + update(mid + 1, end, here * 2 + 1, index);
}

int query(int value) {
	int start = 0, end = N-1, here = 1;
	while (start < end) {
		int mid = (start + end) / 2;
		if (value <= tree[here * 2]) {
			// 왼쪽 서브트리 값보다 같거나 작다면 왼쪽 서브트리로 이동.
			end = mid;
			here = here * 2;
		}
		else {
			// 왼쪽 서브 트리 값보다 크다면 왼쪽 서브 트리 값을 뺀 후 오른쪽 서브트리로 이동.
			// 주어진 수열이 전부 자연수이고, 각 다른 숫자이기 때문에 규칙을 항상 지킨다면 이 조건이 위배되는 일은 없다.
			value -= tree[here * 2];
			start = mid + 1;
			here = here * 2 + 1;
		}
	}
	return start;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> N;
	arr.assign(N, 0);
	tree.assign(1 << int(ceil(log2(N)) + 1), 0);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	init(0, N - 1, 1);
	// 구간 업데이트
	vector<int> result(N);
	for (int i = 0; i < N; i++) {
		int index = query(arr[i] + 1);
		result[index] = i + 1;
		update(0, N - 1, 1, index);
	}

	// 정답 출력
	for (int i = 0; i < N; i++) {
		cout << result[i] << '\n';
	}
	
	return 0;
}
