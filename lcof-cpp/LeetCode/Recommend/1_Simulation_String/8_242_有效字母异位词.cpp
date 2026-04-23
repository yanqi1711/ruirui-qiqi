class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) 
            return false;
        int freq[26]={0};
        for(char c: s)
            freq[c-'a'] +=1;
        for(char c:t)
        {
            freq[c-'a']-=1;
            if(freq[c-'a'] <0)
                return false;
        }
        return true;
    }
};