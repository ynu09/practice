#include <iostream>

using namespace std;

/*
1. 변수의 자료형
2. 변수의 이름 
    - 숫자로 시작 불가 (ex-77aaa)
    - c++ 키워드 불가 (ex-return)
    - white space 사용 불가 (ex-spacebar, enter, tab 등의 여백)
3. 변수가 어디에 저장되는가 (메모리 영역)? => 컴파일러가 자동으로 결정(매칭)해줌
*/
int main() {
    // 변수는 사용되기 이전에 정의돼야 한다
    int a; // 변수 선언
    a = 7; // 값 대입 

    int b = 3; // "초기화": 선언과 동시에 값 대입
    
    cout << "a=" << a << ", b=" << b << endl; // a=7, b=3
    
    // 변수는 변할 수 있는 수 (<-> 상수)
    a = 5;
    b = 10;

    cout << "a=" << a << ", b=" << b << endl; // a=5, b=10

    // 주소값 확인(3번)
    cout << "a=" << &a << ", b=" << &b << endl;
    
    return 0;
}


