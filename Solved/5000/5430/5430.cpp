#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <sstream>
#include <string>
#include <queue>
#include <deque>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int T; cin >> T;
	while (T--) {
		string cmd, str;
		int n;
		cin >> cmd >> n >> str;
		
		int num = 0;

		deque<int> arr;
		for (char c : str) {
			if (c == '[' || c == ']') continue;
			if ('0' <= c && c <= '9') {
				num = num * 10 + (c - '0');
			}
			else {
				arr.push_back(num);
				num = 0;
			}
		}
		if (num > 0) arr.push_back(num);

		//for (int tmp : arr) {
		//	cout << tmp << " ";
		//}
		bool IsReverse = false;
		bool status = false;
		for (char c : cmd) {
			if (c == 'R') {
				IsReverse = !IsReverse;
				continue;
			}
			if (arr.empty()) {
				status = true;
				break;
			}
			if (IsReverse) {
				arr.pop_back();
			}
			else {
				arr.pop_front();
			}
		}
		if (status) {
			cout << "error\n";
			continue;
		}/*
		else if (arr.empty()) {
			cout << "[]\n";
			continue;
		}*/

		string result = "[";
		int size = arr.size();
		for (int i = 0; i < size; i++) {
			if (IsReverse) {
				result += to_string(arr.back());
				arr.pop_back();
			}
			else {
				result += to_string(arr.front());
				arr.pop_front();
			}
			if (i != size - 1) result += ',';
		}
		result += ']';
		cout << result << "\n";
	}
	return 0;
}
