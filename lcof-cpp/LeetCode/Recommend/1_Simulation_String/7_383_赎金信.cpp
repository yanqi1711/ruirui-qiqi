class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
     // 如果ransomNote比magazine长，肯定无法构造
        if (ransomNote.length() > magazine.length()) {
            return false;
        }
        
        // 初始化频率数组（26个小写字母）
        int freq[26] = {0};
        
        // 统计magazine中各字符出现次数
        for (char c : magazine) {
            freq[c - 'a']++;
        }
        
        // 检查ransomNote中的字符是否可用
        for (char c : ransomNote) {
            // 减少字符计数，若计数<0说明字符不足
            if (--freq[c - 'a'] < 0) {
                return false;
            }
        }
        
        // 所有字符均满足要求
        return true;
    }
};