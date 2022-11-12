#include <iostream>

using namespace std;
int dp[501][501];
int d[501];

int min(int a, int b) { return (a < b) ? a : b;}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    int a, b;
    for(int i=1; i<=n;i++){
        cin >> a >> b;
        d[i-1] = a;
        d[i] = b;
    }


    for (int diagonal=1; diagonal < n; diagonal++){
        for (int i = 1; i <= n-diagonal; i++) {
            int j = i + diagonal;
            dp[i][j] = 987654321;
            for (int k = i; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + d[i - 1] * d[k] * d[j]);
            }
        }
    }

//    for(int i = 0; i<=n; i++){
//        for (int j = 0; j <= n; j++) {
//            cout << dp[i][j] << " ";
//        }
//        cout << "\n";
//    }

    cout << dp[1][n];

    return 0;
}