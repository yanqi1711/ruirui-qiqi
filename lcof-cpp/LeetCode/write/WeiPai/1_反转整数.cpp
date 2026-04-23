#include <iostream>
using namespace std;
class Solution
{
public:
    int reverse(int x)
    {
        int res = 0;
        while (x)
        {
            // C++/Java截断取模 所以 -11%10 = -1 但是python是-11%10=9 是取模定义不同 python是数学定义
            int bit = x % 10;
            if (res > 214748364 || (res == 214748364 && bit > 7))
                return 0;
            if (res < -214748364 || (res == -214748364 && bit < -8))
                return 0;
            res = res * 10 + bit;
            x /= 10;
        }
        return res;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.reverse(-123) << endl;
    cout << -123 % 10 << endl;

    getchar();
    return 0;
}
