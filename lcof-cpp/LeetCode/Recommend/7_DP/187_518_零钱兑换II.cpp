class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<unsigned long> dp(amount+1, 0);
        dp[0] = 1;// 不选
        // 找到所有coin的情况
        for(auto& coin: coins)
        {
            for(int j = coin; j<= amount;++j)
            dp[j] += dp[j-coin];
        }
        return dp[amount];
    }
};