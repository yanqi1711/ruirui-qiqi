#include <algorithm>
class Solution {
public:
    // abcd => dp[d] = 4(d, cd bcd abcd)
    int findSubstringInWraproundString(string s) {
        // 对应26个字母所有的情况,dp是以字母结尾的所有字串数量
        vector<int> dp(26,0);
        int count = 0;
        for(int i=0;i<s.size();++i)
        {
            if(i>0 && ( (s[i]-s[i-1]+26)%26 ==1 )) // +26 防止负数
                count +=1;
            else
                count = 1;
            //每次获得dp[以字母结尾的数目]
            dp[s[i]-'a'] = std::max(count, dp[s[i]-'a']); // max去除重复的数量
        }
        return std::accumulate(dp.begin(), dp.end(), 0);
    }
};