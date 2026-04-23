class Solution {
public:
    int firstUniqChar(string s) {
        std::unordered_map<char, std::pair<int, int>> m; // {char: {first_index, count}}
        // 第一次遍历：统计字符频率和首次出现位置
        for(int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if(m.find(c) == m.end()) { // 字符不存在
                m[c] = std::make_pair(i, 1); // 记录首次位置，计数=1
            } else { // 字符已存在
                m[c].second++; // 只增加计数（不修改位置）
            }
        }
        
        // 第二次遍历：按字符串顺序查找第一个唯一字符
        for(int i = 0; i < s.size(); ++i) {
            if(m[s[i]].second == 1) {
                return i;
            }
        }
        return -1;
    }
};
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<int, int> frequency;
        for (char ch: s) {
            frequency[ch]++;
        }
        for (int i = 0; i < s.size(); i++) {
            if (frequency[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};