class Solution {
public:
    char findTheDifference(string s, string t) {
        std::unordered_map<char, int> m;
        for (char ch: s) {
            m[ch]++;
        }
        for (char ch: t) {
            m[ch]--;
        }
        for(auto& pair : m)
            if(pair.second == -1)
                return pair.first;
        return ' ';
    }
};