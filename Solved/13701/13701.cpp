#include <iostream>
using namespace std;
int arr[1 << 20];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int V;
    while (cin >> V){
        int Q = V / 32;
        int R = 1 << (V % 32);
        if (!(arr[Q] & R)){
            arr[Q] += R;
            cout << V << " ";
        }
    }
    return 0;
}
