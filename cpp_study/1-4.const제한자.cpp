#include <iostream>

using namespace std;

/*
원의 넓이를 구하는 프로그램
- 반지름 * 반지름 * pi(상수)
- 상수는 const 키워드를 사용하여 선언
- 값 변경 불가 (대입x, 초기화 방식으로 작성)
*/  
int main() {
    const float PIE = 3.1415926535;

    int r = 3;
    // float s = r * r * 3.14;
    float s = r * r * PIE;

    cout << "원의 넓이: " << s << endl;

    return 0;
}