/*
输入 m×n 网格，x 表示旱地，o 表示水田。对于每个旱地格子，
计算“其四个方向上连通的水田格数之和 + 自身（+1）”。
水田格按 4 邻域连通。最终输出矩阵：旱地输出该值，水田输出 0。
sample:
3 3
xoo
oxo
xox
输出:
500
060
305
*/

/*
自己错误点:
错误 1：递归检查对象错位——没先判断“自己”
错误 2：访问标记复原导致重复计算
重点:
补充：什么时候“要回溯恢复标记”？
| 题目类型                | 是否回溯恢复标记 | 举例             |
| ------------------- | -------- | -------------- |
| **路径搜索（找路径、所有方案）**  | ✅ 是      | 全排列、迷宫寻路、八皇后问题 |
| **区域/连通块搜索（求区域大小）** | ❌ 否      | 岛屿数量、感染区域、染色问题 |

*/
#include <iostream>
#include <vector>
using namespace std;

int dfs(vector<vector<int>> &v, int i, int j, int m, int n)
{
    if (i < 0 || j < 0 || i >= m || j >= n) //
        return 0;
    if (v[i][j] == 1)
        return 0; // 旱地或已访问

    v[i][j] = 1; // 标记已访问（水田临时改为旱地防止重复访问）

    int cnt = 1;
    cnt += dfs(v, i - 1, j, m, n);
    cnt += dfs(v, i + 1, j, m, n);
    cnt += dfs(v, i, j - 1, m, n);
    cnt += dfs(v, i, j + 1, m, n);

    return cnt;
}

int main()
{
    int m, n;
    cin >> m >> n;
    vector<vector<int>> v(m, vector<int>(n));

    for (int i = 0; i < m; ++i)
    {
        string s;
        cin >> s;
        for (int j = 0; j < n; ++j)
            v[i][j] = (s[j] == 'x'); // x=1, o=0
    }

    vector<vector<int>> res(m, vector<int>(n, 0));

    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (v[i][j] == 1) // 旱地
            {
                int total = 1;                // 包含自己
                vector<vector<int>> copy = v; // 拷贝，用于独立DFS 因为每一个结点都是独立的
                total += dfs(copy, i - 1, j, m, n);
                total += dfs(copy, i + 1, j, m, n);
                total += dfs(copy, i, j - 1, m, n);
                total += dfs(copy, i, j + 1, m, n);
                res[i][j] = total;
            }
        }
    }

    for (auto &row : res)
    {
        for (auto &x : row)
            cout << x;
        cout << "\n";
    }

    return 0;
}
