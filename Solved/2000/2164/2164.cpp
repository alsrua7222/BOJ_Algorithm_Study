#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int N; cin >> N;
	if (N == 1) {
		cout << 1;
		return 0;
	}
	queue<int> q;
	if (N % 2 != 0) {
		q.push(N);
	}
	for (int i = 2; i <= N; i += 2) {
		q.push(i);
	}

	while (q.size() != 1) {
		q.pop();
		q.push(q.front());
		q.pop();
	}
	cout << q.front();
	
	return 0;
}
