class Solution {
public:
    string reverseWords(string s) {
        std::string res;
        int n = s.size();
        int i = n-1;
        while(i>=0)
        {
            // 尾部空格 第一次是尾部空格 后面实际上中间所有空格都走了
            while(i>=0 && s[i] == ' ') i--;
            if(i<0) break; // 处理完了

            int j = i; //标记尾部字符
            while(i>=0 && s[i] != ' ') i--;
            // 此时i指向空格 substr (index, length)-->是截取的长度
            res += s.substr(i+1 , j-i);
            res += ' ';
        }
        if(!res.empty()) res.pop_back();
        return res;
    }
};