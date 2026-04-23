class Solution {
public:
    int countBinarySubstrings(string s) {
         // 统计每一段区间的0,1个数 那么01组合一定在这之间 并且取最小值
         // 0011110 ==> 2 4 1 ==?2+1=3 因为长度就代表不同情况
        if (s.empty()) return 0; // 处理空字符串
        
        int ans = 0;
        int prev_len = 0;    // 前一个连续段的长度
        int cur_len = 1;      // 当前连续段的长度（从第一个字符开始）
        
        for (int i = 1; i < s.size(); ++i) {
            if (s[i] == s[i - 1]) {
                ++cur_len;   // 相同字符，当前段长度增加
            } else {
                ans += min(prev_len, cur_len); // 遇到新段，累加相邻段的贡献
                prev_len = cur_len;             // 更新前段长度
                cur_len = 1;                    // 重置当前段长度
            }
        }
        ans += min(prev_len, cur_len); // 处理最后一段
        return ans;
    }
};