#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    // 4 3 2 1 0 -1 -2 -3 -4
    int cnt = 1;
    for(int i=n-1; i>-n; i--){
        for(int j=0; j<abs(i); j++){
            cout << " ";
        }
        for(int k=0; k<cnt; k++){
            cout << '*';
        }
        if (i > 0){
            cnt += 2;
        } else{
            cnt -= 2;
        }

        cout << endl;
    }
}