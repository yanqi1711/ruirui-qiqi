class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;
        int maxFreq=0;
        for(char &ch: s)
        {
            ++freq[ch];
            maxFreq = std::max(freq[ch], maxFreq);
        }

        // 桶排序 频率=索引 必须用二维 
        // 字符串中可能有两个字符都出现了3次，那么它们都应该被放在频率为3的桶中 
        // 一维无法处理以上情况
        vector<vector<char>> v(maxFreq+1);
        for(const auto& [ch, count]: freq)
            v[count].emplace_back(ch);
        
        string result;
        result.reserve(s.size());  // 关键优化：避免多次分配
        // 遍历二维数组即可
        for(int count = maxFreq; count>0;--count)
        {
            for(auto& ch:v[count])
                result.append(count, ch);
        }
        return result;
    }
};