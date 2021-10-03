#include <iostream>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N; cin >> N;
    int answer = 0;
    for(int first = 1; first <= N / 3; first++){
        for(int second = (N - first) / 2; second >= first; second--){
            if (N - first - second < first + second){
                answer++;
            }
            else{
                break;
            }
        }
    }
    cout << answer;
}
