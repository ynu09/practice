#include <iostream>
#include <climits>

using namespace std;

/*
정수형: 소수부가 없는 수 (음의 정수, 0, 양의 정수)
- 종류: short < int < long < long long (표현할 수 있는 수의 크기가 다름)
- 메모리 효율 고려하여 사용
*/
int main() {
    // 4가지의 데이터형 (각 자료형이 저장할 수 있는 최대 크기)
    short n_short = SHRT_MAX;
    int n_int = INT_MAX;
    long n_long = LONG_MAX;
    long long n_llong = LLONG_MAX;

    cout << "short는 " << sizeof n_short << "바이트이다." << endl;
    cout << "이 바이트의 최대값은 " << n_short << " 이다." << endl;
    
    cout << "int는 " << sizeof n_int << "바이트이다." << endl;
    cout << "이 바이트의 최대값은 " << n_int << " 이다." << endl;
    
    cout << "long은 " << sizeof n_long << "바이트이다." << endl;
    cout << "이 바이트의 최대값은 " << n_long << " 이다." << endl;
    
    cout << "long long은 " << sizeof n_llong << "바이트이다." << endl;
    cout << "이 바이트의 최대값은 " << n_llong << " 이다." << endl;

    /*
    [음의 정수를 사용하지 않을 경우, unsigned 붙이면 보다 넓은 범위 사용 가능]
    unsigned: 음의 값을 저장할 필요가 없어져 변수형이 저장할 수 있는 최댓값 늘릴 수 있음
    short: -32768 ~ 32767 -> unsigned short: 0 ~ 65535 (양의 영역 늘어남)
    */
    unsigned short n_ushort = USHRT_MAX;
    cout << "unsigned short는 " << sizeof n_ushort << "바이트이다." << endl;
    cout << "이 바이트의 최대값은 " << n_ushort << " 이다." << endl;

    // 범위 밖의 수(ex: -1) 입력 시, 반대편으로 넘어감 
    unsigned short a = -1;
    cout << "-1: " << a << endl; // 65535
    unsigned short b = -2;
    cout << "-2: " << b << endl; // 65534

    return 0;
}