#include <iostream>

using namespace std;

/*
원의 넓이를 구하는 프로그램
- 반지름 * 반지름 * pi
*/  
int main() {
    int r = 3;
    float s = r * r * 3.14;

    cout << "원의 넓이: " << s << endl;

    return 0;
}