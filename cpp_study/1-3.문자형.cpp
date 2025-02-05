#include <iostream>

using namespace std;

/*
char: 작은 문자형 -> 컴퓨터는 숫자로 받아들임
*/
int main() {
    // 숫자로 문자 표현
    int a = 77;
    char b = a;
    cout << "int a: " << a << endl; // 77
    cout << "char b: " << b << endl; // M


    // 단순히 문자 출력 ("" 사용 불가)
    char c = 'a';
    /*
    char c;
    c = 'a';
    */
    cout << "char c: " << c << endl; // a

    return 0;
}