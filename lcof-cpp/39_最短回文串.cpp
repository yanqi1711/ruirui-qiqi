#include <string>
#include <vector>
#include <algorithm>
using namespace std;
class Solution
{
public:
    string shortestPalindrome(string s)
    {
        if (s.size() < 2)
            return s;
        // 将字符串翻转，找原字符串和翻转之后的字符串的最长公共子串，不匹配的部分就是要添加的字符。

        // 1.获得翻转之后的字符串
        string str = s;
        reverse(str.begin(), str.end());

        // 2.查找最长的公共子串 , KMP算法可以满足查找并达到O（n）的要求
        int len = s.size();
        vector<int> nextVal(len, 0);
        getNextVal(nextVal, s);

        int j = 0, i = 0;
        // 把反转后的字符串为匹配串 s为模式串 找到最后 i就是公共回文串
        for (i = 0; i < str.size(); i++)
        {
            while (j > 0 && str[i] != s[j])
                j = nextVal[j - 1];
            if (str[i] == s[j])
                j++;
            if (j == s.size())
                return s;
        }
        //  abcd 找到1 所以截取 bcd 反转再加原来字符串s
        string add_pre = s.substr(j);
        reverse(add_pre.begin(), add_pre.end());
        string ans = add_pre + s;
        return ans;
    }

private:
    void getNextVal(vector<int> &nextVal, const string &str)
    {
        int j = 0;
        nextVal[0] = 0;
        for (int i = 1; i < str.size(); i++)
        {
            while (j > 0 && str[i] != str[j])
                j = nextVal[j - 1];
            if (str[i] == str[j])
                j++;
            nextVal[i] = j;
        }
    }
};