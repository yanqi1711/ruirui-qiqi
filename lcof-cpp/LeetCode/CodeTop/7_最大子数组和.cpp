class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        if (nums.size() < 1)
            return 0;
        if (nums.size() == 1)
            return nums[0];
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        int maxValue = nums[0];
        for (int i = 1; i < nums.size(); ++i)
        {
            dp[i] = std::max(dp[i - 1] + nums[i], nums[i]);
            maxValue = maxValue > dp[i] ? maxValue : dp[i];
        }
        return maxValue;
    }
};