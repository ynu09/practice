#include <iostream>

using namespace std;

/*
char: 작은 문자형 -> 컴퓨터는 숫자로 받아들임
- 하나의 문자만 저장 가능
null 문자: '\0' (문자열 출력 범위 지정)
*/
int main() {
    // 숫자로 문자 표현
    int a = 77;
    char b = a;
    cout << "int a: " << a << endl; // 77
    cout << "char b: " << b << endl; // M


    /* 
    단순히 문자 출력 ("" 사용 불가)
    "" >> 명시적으로 null 문자 포함됨
    ex) char c = "a"; >> a\0 ; a, null 문자 둘 다 저장 불가
    */
    char c = 'a';
    /*
    char c;
    c = 'a';
    */
    cout << "char c: " << c << endl; // a

    // 배열로 문자열 출력 ('\0' 필수 ; 없을 시, 뒤에 더 출력됨)
    char d[]= {'a', 'b', 'c', '\0'};
    cout << "char d: " << d << endl; // abc

    return 0;
}