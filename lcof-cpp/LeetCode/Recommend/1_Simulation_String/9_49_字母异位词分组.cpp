class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> groups;
        
        for (string &s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            groups[key].emplace_back(s);  // 使用emplace_back避免拷贝
        }
        
        for (auto &group : groups) {
            result.emplace_back(group.second);  // 使用emplace_back
        }
        
        return result;
    }
};