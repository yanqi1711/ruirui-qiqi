class Solution {
public:
    void reverseString(string& s, int start, int end) {
        int left = start, right = end - 1;
        while (left < right) {
            swap(s[left], s[right]);
            left++;
            right--;
        }
    }
    string reverseStr(string s, int k) {
        const int n = s.size();
        for(int i =0; i< n; i+= 2*k)
        {
            // 最后大于k 反转前k个 小于就全部
            const int rev_end = std::min(i+k, n);
            reverseString(s, i, rev_end);
        }
        return s;
    }
};