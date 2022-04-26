#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
typedef struct info {
	string s;
	int d, m, y;
}info;
vector<info> v;

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

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int T; cin >> T;
	while (T--) {
		string name;
		int day, month, year;
		cin >> name; cin >> day; cin >> month; cin >> year;
		v.push_back({ name, day, month, year });
	}
	sort(v.begin(), v.end(), compare);
	cout << v.back().s << "\n" << v.front().s << "\n";
	return 0;
}
