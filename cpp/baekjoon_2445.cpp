#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for(int i=1; i<n+1;i++){
        for(int j=1; j<i+1; j++){
            cout << "*";
        }
        for(int k=0; k<(n*2)-(i*2); k++){
            cout << " ";
        }

        for(int j=1; j<i+1; j++){
            cout << "*";
        }
        cout << endl;
    }

    for(int i=n-1; i>0; i--){
        for(int j=0; j<i; j++){
            cout << "*";
        }
        for(int k=0; k<(n*2)-(i*2); k++){
            cout << " ";
        }

        for(int j=0; j<i; j++){
            cout << "*";
        }
        cout << endl;
    }
}
