#include <sstream>
#include <sstream>

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::istringstream iss(s);
        std::ostringstream oss;
        std::string word;
        
        // 处理第一个单词（前面不加空格）
        if (iss >> word) {
            std::reverse(word.begin(), word.end());
            oss << word;
        }
        
        // 处理后续单词（前面加空格）
        while (iss >> word) {
            std::reverse(word.begin(), word.end());
            oss << " " << word;
        }
        
        return oss.str();
    }
};

// 太慢了
class Solution {
public:
    void reverseWord(string &word)
    {
        int left = 0,right = word.size()-1;
        while(left < right)
        {
            std::swap(word[left], word[right]);
            ++left;
            --right;
        }
    }
    string reverseWords(string s) {
        std::istringstream iss(s);
        std::vector<std::string> tokens(
        std::istream_iterator<std::string>{iss},
        std::istream_iterator<std::string>{}
        );
        s.clear();
        int count = tokens.size()-1;
        for(int i = 0; i<tokens.size(); ++i)
            {
                reverseWord(tokens[i]);
                s+=tokens[i];
                if(i!=count)
                    s+=" ";
            }
        return s;
    }
};