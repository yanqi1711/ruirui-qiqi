class Solution
{
public:
    string longestPalindrome(string s)
    {
        int res_len = 0;
        int res_start = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            // bab
            int L = i, R = i;
            while (L >= 0 && R < s.size() && s[L] == s[R])
            {
                if (R - L + 1 > res_len)
                {
                    res_len = R - L + 1;
                    res_start = L;
                }
                --L;
                ++R;
            }
            L = i;
            R = i + 1;
            while (L >= 0 && R < s.size() && s[L] == s[R])
            {

                if (R - L + 1 > res_len)
                {
                    res_len = R - L + 1;
                    res_start = L;
                }
                --L;
                ++R;
            }
        }

        return s.substr(res_start, res_len);
    }
};