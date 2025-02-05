#include <iostream>

using namespace std;

// 문자열: 문자의 열(집합)
int main() {
    char a[6] = {'H', 'e', 'l', 'l', 'o', '\0'}; // 문자열 "Hello"를 저장할 수 있는 배열 a 선언
    cout << a << endl; // "Hello"

    char b[] = "Hello";
    // [] 배열 사이즈 비워두면 컴파일러가 자동으로 배열에 알맞은 사이즈 할당
    // ""는 null 문자 포함하고 있음
    cout << b << endl; // "Hello"

    return 0;
}