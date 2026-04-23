class Solution
{
public:
    int Add(int num1, int num2)
    {
        while (num2 != 0)
        {
            // 计算不进位的和
            int sum = num1 ^ num2;
            // 计算进位
            int carry = (num1 & num2) << 1;
            // 更新num1和num2
            num1 = sum;
            num2 = carry;
        }
        return num1;
    }
};