#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    vector<int> largestDivisibleSubset(vector<int> &nums)
    {
        vector<vector<int>> dp;
        sort(nums.begin(), nums.end());
        dp.emplace_back(vector<int>{nums[0]}); // 创建一个包含 i 的 vector<int> 并添加到 dp
        // 找到第i个最大的整除子集
        vector<int> maxVector{nums[0]};
        for (int i = 1; i < nums.size(); ++i)
        {
            vector<int> v{nums[i]};
            for (int j = i - 1; j >= 0; --j)
            {
                if (nums[i] % nums[j] == 0)
                {
                    if (v.size() > dp[j].size())
                        continue;
                    v.clear();
                    // 应该加入他dp数组里面的元素 而不是本身
                    for (auto k : dp[j])
                        v.emplace_back(k);
                    v.emplace_back(nums[i]);
                }
                if (maxVector.size() < v.size())
                    maxVector = v;
            }
            dp.emplace_back(v);
        }
        // 打印dp
        for (auto v1 : dp)
        {
            for (auto v2 : v1)
            {
                cout << v2 << " ";
            }
            cout << endl;
        }
        return maxVector;
    }
};