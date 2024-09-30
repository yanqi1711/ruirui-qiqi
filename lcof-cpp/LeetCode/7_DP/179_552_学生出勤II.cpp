#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;
class Solution
{
public:
    static constexpr int MOD = 1'000'000'007;
    // 矩阵乘法
    vector<vector<long>> multiply(vector<vector<long>> matrix1, vector<vector<long>> matrix2)
    {
        // 行                列                     需要相加得次数
        int rows = matrix1.size(), columns = matrix2[0].size(), count = matrix2.size();
        vector<vector<long>> v(rows, vector<long>(columns));

        for (int i = 0; i < rows; ++i)
        {
            for (int j = 0; j < columns; ++j)
            {
                for (int k = 0; k < count; ++k)
                {
                    v[i][j] += matrix1[i][k] * matrix2[k][j];
                    v[i][j] %= MOD;
                }
            }
        }
        return v;
    }

    vector<vector<long>> quickpow(vector<vector<long>> mat, int n)
    {
        vector<vector<long>> res = {{1, 0, 0, 0, 0, 0}};
        while (n > 0)
        {
            if ((n & 1) == 1)
                res = multiply(res, mat);
            n >>= 1;
            mat = multiply(mat, mat);
        }
        return res;
    }

    int checkRecord(int n)
    {
        vector<vector<long>> mat = {
            {1, 1, 0, 1, 0, 0},
            {1, 0, 1, 1, 0, 0},
            {1, 0, 0, 1, 0, 0},
            {0, 0, 0, 1, 1, 0},
            {0, 0, 0, 1, 0, 1},
            {0, 0, 0, 1, 0, 0}};
        vector<vector<long>> ans = quickpow(mat, n);
        // 0 是一个整数零 ll 表示该值的类型是 long long
        long sum = accumulate(ans[0].begin(), ans[0].end(), 0ll);
        return (int)(sum % MOD);
    }
};
int main(int argc, char const *argv[])
{
    auto s = Solution();
    auto a = s.checkRecord(2);
    cout << a << endl;
    return 0;
}
