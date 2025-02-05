#include <iostream>

using namespace std;

/*
C++은 복합데이터형을 제공
- 복합데이터형: 기본 정수형과 부동소수점형의 조합
- 사용자 정의대로 새로운 데이터형을 만들 수 있음 

배열(array): 같은 데이터형의 집합 
- typeName arrayName[arraySize];
- arraySize: 배열의 크기 (몇개 저장할 수 있는지)
*/
int main() {
    // 배열 부분 사용 가능
    short month[12] = {1, 2, 3}; // 12개의 short형 데이터를 저장할 수 있는 배열 month 선언

    cout << month[0] << endl; // 1 (인덱스로 관리) 

    // 대입하지 않은 값은 0으로 설정됨
    cout << month[3] << endl; // 0 출력

    /*
    배열의 크기를 지정하지 않으면 초기화된 값만큼 크기가 설정됨
    - ex) short month[] = {1, 2, 3}; (3개)
    - 이 경우, 4번째 값부턴 사용 불가
    */

    return 0;
}