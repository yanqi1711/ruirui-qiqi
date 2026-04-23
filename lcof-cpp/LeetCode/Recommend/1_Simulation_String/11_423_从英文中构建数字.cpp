/*
 0: z (只在zero中出现)
 2: w (只在two中出现)
 4: u (只在four中出现)
 6: x (只在six中出现)
 8: g (只在eight中出现)
*/
/*
v[3] = count('h') - v[8]   // h在three和eight中
v[7] = count('s') - v[6]   // s在six和seven中
v[5] = count('v') - v[7]   // v在five和seven中  或者用f：v[5]=count('f')-v[4]（
两种方法都可以，但必须选择一种，这里我们用两种方法中的一种，为了不与v[4]冲突，我们用字母v）
*/
 
class Solution {
public:
    string originalDigits(string s) {
        vector<int> v(10, 0); // 只需10个数字（0-9）
        // 先统计唯一字母的数字
        v[0] = count(s.begin(), s.end(), 'z'); // zero (z)
        v[2] = count(s.begin(), s.end(), 'w'); // two (w)
        v[4] = count(s.begin(), s.end(), 'u'); // four (u) 
        v[6] = count(s.begin(), s.end(), 'x'); // six (x)
        v[8] = count(s.begin(), s.end(), 'g'); // eight (g)
        
        // 再统计依赖其他字母的数字
        v[3] = count(s.begin(), s.end(), 'h') - v[8]; // three (h - eight的h)
        v[5] = count(s.begin(), s.end(), 'f') - v[4]; // five (f - four的f) 
        v[7] = count(s.begin(), s.end(), 's') - v[6]; // seven (s - six的s)
        
        // 最后统计剩余数字（注意修正）
        v[1] = count(s.begin(), s.end(), 'o') - v[0] - v[2] - v[4]; // one (o - zero/two/four的o)
        v[9] = count(s.begin(), s.end(), 'i') - v[5] - v[6] - v[8]; // nine (i - five/six/eight的i)
        
        // 构建结果字符串
        string result;
        for (int i = 0; i <= 9; i++) {
            result.append(v[i], '0' + i); // 添加v[i]个数字字符
        }
        return result;
    }
};