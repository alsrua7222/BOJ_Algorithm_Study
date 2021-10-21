#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int T;
	cin >> T;
	string cmd;
	queue<int> Queue;
	while (T--){
		cin >> cmd;
		if (cmd == "push") {
			int n; cin >> n;
			Queue.push(n);
		}
		else {
			if (cmd[0] == 'f') {
				if (!Queue.empty()) cout << Queue.front();
				else cout << -1;
			}
			else if (cmd[0] == 'b') {
				if (!Queue.empty()) cout << Queue.back();
				else cout << -1;
			}
			else if (cmd[0] == 's') {
				cout << Queue.size();
			}
			else if (cmd[0] == 'e') {
				if (!Queue.empty()) cout << 0;
				else cout << 1;
			}
			else if (cmd[0] == 'p') {
				if (!Queue.empty()) {
					cout << Queue.front();
					Queue.pop();
				}
				else cout << -1;
			}
			cout << "\n";
		}
	}
	return 0;
}
