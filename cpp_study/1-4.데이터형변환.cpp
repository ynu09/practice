#include <iostream>

using namespace std;

/*
데이터형 변환: 자동으로 데이터형 바꿔줌
- >> 특정 데이터형의 변수에 다른 데이터형의 값을 대입할 때
- 수식에 데이터형을 혼합하여 사용했을 때
- 함수에 매개변수를 전달할 때
*/
int main() {
    // 특정 데이터형의 변수에 다른 데이터형의 값을 대입할 때
    int a = 3.141592;
    cout << "a: " << a << endl; // 3

    /*
    강제적으로 데이터형 변환
    ex) typeName(a), (typeName)a
    - typeName: 변환하고자 하는 데이터형
    - a: 변환할 변수 
    */
    char ch = 'M';
    cout << (int)ch << " " << int(ch) << endl; // 77 77

    // C++
    // static_cast<typeName> (동일하게 동작)
    cout << static_cast<int>(ch) << endl; // 77

    return 0;
}