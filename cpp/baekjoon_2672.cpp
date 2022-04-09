#include<bits/stdc++.h>

#define all(v) v.begin(), v.end()
#define FOR(i, j, k) for(int i = j; i<=k; i++)
using namespace std;

using ll = long long;

struct sero {
    int x;
    int y1, y2;
    int chk;
    bool operator < (sero b) {
        if(x == b.x) {
            return chk < b.chk;
        }
        else return x < b.x;
    }
};

int A[20001];

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int N;
    cin >> N;
    vector<sero> v;
    FOR(i, 1, N){
        double a, b, c, d;
        cin >> a >> b >> c >> d;
        a *= 10; b *= 10; c *= 10; d *= 10;
        sero s;
        s.x = (int)a;
        s.y1 = (int)b;
        s.y2 = (int)(b + d);
        s.chk = 1;
        v.push_back(s);
        s.x = (int)(a + c);
        s.chk = -1;
        v.push_back(s);
    }
    sort(v.begin(), v.end());
    ll ans = 0;
    int lx = 0;
    for(sero s : v) {
        int cnt = 0;
        FOR(i, 0, 20000){
            if(A[i] > 0) cnt++;
        }
        ans += cnt * (s.x - lx);
        FOR(i, s.y1+1, s.y2){
            if(s.chk == 1)
                A[i]++;
            else
                A[i]--;
        }
        lx = s.x;
    }

    if(ans % 100 == 0)
        cout << ans / 100;
    else {
        cout << fixed;
        cout.precision(2);
        cout << ans / 100.0;
    }

}