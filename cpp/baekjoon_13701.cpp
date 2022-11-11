#include <iostream>

using namespace std;
int exist[(1<<25) / 32];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    while (~scanf("%d", &n)) {
        int q = n / 32;
        int r = 1 << (n % 32);

        if (!(exist[q] & r)){
            exist[q] += r;
            cout << n << " ";
        }
    }


    return 0;
}