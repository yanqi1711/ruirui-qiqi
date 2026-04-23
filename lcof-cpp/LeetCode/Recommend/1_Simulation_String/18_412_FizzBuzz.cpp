class Solution {
public:
    string toString(int n)
    {
	    stringstream ss;    // 1. 创建空的字符串流对象
        ss << n;            // 2. 将整数 n 插入流中（转换为字符串）
        return ss.str();    // 3. 通过 str() 方法获取流中的字符串并返回
    }
    vector<string> fizzBuzz(int n) {
        vector<string> res(n);
        int num3=3,num5=5,num15=15;
        for(int i=1; i<=n;++i)
        {
            if(i == num15) // 优先满足15
            {
                res[i - 1] = "FizzBuzz";
                num15 += 15;
                num5 += 5; //同时这两个数也要增加
                num3 += 3;
            }
            else if(i == num5)
            {
                res[i-1] = "Buzz";
                num5 += 5;
            }
            else if(i == num3)
            {
                res[i-1] = "Fizz";
                num3 += 3;
            }
            else
            {
                res[i-1] = toString(i);
            }
        }
        return res;
    }
};