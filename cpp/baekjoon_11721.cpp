#include <iostream>
#include <cstring>

using namespace std;

int main() {

    string a;

    getline(cin, a);

    for (int i = 0; i < a.size(); i++) {
        cout << a[i];
        if( (i+1) % 10 ==0 ){
            cout << endl;
        }
    }

    return 0;
}
