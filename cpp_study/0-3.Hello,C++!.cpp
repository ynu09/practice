#include <iostream>
/* 
#include: 전처리 지시자 (다양한 함수들 정의하고 있음)
<iostream>: 함수 원형 정의 (ex:cout, endl)
*/

using namespace std;
/*
만약 using namespace가 없다면?
밑에서 함수 사용 시, std::cout, std::endl 붙여줘야 함
(std는 iostream의 namespace)
*/
// ';': 종결자의 의미 (중간에 빈칸이 얼마나 있든 상관x)

// main 함수는 무조건 존재해야 함 (실행부)
int main() {
    cout << "Hello, World!" << endl;
    /*
    cout: 콘솔에 출력 역할
    endl: 줄바꿈 역할
    <<: 데이터의 흐름
    */
    return 0;
}