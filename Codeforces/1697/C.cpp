#include <bits/stdc++.h>
using namespace std;

#define FAST { ios :: sync_with_stdio(false); cin.tie(0); cout.tie(0); }
#define pb push_back
#define ll long long 
#define vi vector<int>
#define vll vector<long long>
#define f(i,a,b) for(ll i=a;i<b;i++)
#define pii pair<int,int>
#define pll pair<ll,ll> 
#define endl "\n"
    
   
    
void solve(string& a, string& b, char x, char y, char z) {
        
    bool pos = true;
    int j=0;
    for(int i=0;i< (int)a.size();i++){
        if(a[i] == x){
            pos = false;
            if(j < i) {
                j = i;
            }
            for(; j < (int)a.size(); j++){
                if(b[j] ==y)
                {   
                    char c = b[i];
                    b[i] = b[j];
                    b[j] = c;
                    pos = true;
                    break;
                }
                if(b[j]!=z) break;
            }
            if(!pos) break; 
        }
    }
}

 
int main(){
    FAST;
       
     
    ll t=1;
    cin>>t;
     
    while (t--){
        int n;
        cin>>n;
        
        string a;
        string b;
        cin>>b >> a;
        char check = 'c';
       
        solve(a,b,'c','c','b');
        solve(a,b,'b','b','a');
       
        if(a == b) cout << "YES";
        else cout << "NO";
        cout << endl;
    }
 
    return 0;
}