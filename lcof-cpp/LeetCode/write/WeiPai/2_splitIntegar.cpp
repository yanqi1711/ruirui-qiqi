/*
拆分整数：
给定一个整数n 将其无序拆分为最大数为k的拆分数（n,k不超出100）
要求拆分方案不重复
当n=4,k=4时有5种拆分方案:
1+1+1+1+1
1+1+2
1+3
2+2
4
输入样例:
4 4
5 4
输出:
5
6

递推式:
n>k = f(n,k-1)+f(n-k,k) // 以[4,2]为例，拆分成两种情况，一种是最大数不超过1的拆分方案，一种是包含2的拆分方案
                        // [4,2] = [4,1] + [2,2] 其中[4,1] = 1种方案 拆成 1 1 1 1
                        // [2,2] = 本质是已经拆了1个1所以后面有几个1都不会重复 即:
                        // [2,2] = [2,1] + 自身(2) = 1 + 1 = 2种方案 拆成 1 1 2 和 2 2
                        // 所以[4,2] = 1 + 2 = 3种方案
n<k = f(n,n)
n=k = f(n,k-1)+1 // 因为n=k时 只有自身 所以只需要加1，把自身排除 拆分成n>k的情况
n=1 or k=1 = 1
*/

#include <iostream>
using namespace std;
// 递归
int f(int n, int k)
{
    if (n == 1 || k == 1)
        return 1;
    if (n < k)
        return f(n, n);
    else if (n == k)
        return f(n, k - 1) + 1;
    else
        return f(n, k - 1) + f(n - k, k);
}
int main()
{
    int n, k;
    cin >> n >> k;
    int dp[n + 1][k + 1];
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            dp[i][j] = 0;
        }
    }
    for (int i = 0; i <= k; i++)
    {
        dp[0][i] = 1;
    }
    for (int i = 0; i <= n; ++i)
    {
        for (int j = 0; j <= k; ++j)
        {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= k; j++)
        {
            if (i - j >= 0)
            {
                dp[i][j] = dp[i][j - 1] + dp[i - j][j];
            }
            else
            {
                dp[i][j] = dp[i][j - 1];
            }
        }
    }
    for (int i = 0; i <= n; ++i)
    {
        for (int j = 0; j <= k; ++j)
        {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    cout << dp[n][k] << endl;
    cout << "n=" << n << ",k=" << k << endl;
    cout << f(n, k) << endl;
    cout << "Press any key to continue..." << endl;
    getchar();
    return 0;
}