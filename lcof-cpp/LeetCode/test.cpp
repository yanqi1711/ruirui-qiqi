#include <complex>
#include <ios>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;
struct alignas(4) Test
{
    char a;   // 1 字节
    double b; // 8 字节
    char c;   // 1 字节
};
struct alignas(4) Info2
{
    uint8_t a;
    uint16_t b;
    uint8_t c;
};
int main()
{
    cout << sizeof(Test) << endl;
    cout << sizeof(Info2) << endl;
    return 0;
}
// 64 位输出请用 printf("%lld")