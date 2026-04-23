class Solution
{
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型vector
     * @return int整型vector
     */
    vector<int> FindNumsAppearOnce(vector<int> &nums)
    {
        int sum = 0;
        for (auto &i : nums)
        {
            sum ^= i;
        }
        // 异或规律 相同为0，所以需要找到这2个数不同的位 即sum位为1的
        int target = 1;
        while (0 == (sum & target))
            target <<= 1;

        // 此时target就是不同的分组标记 因为 相同的数一定是同一组
        int a = 0, b = 0;
        for (int x : nums)
        {
            if (x & target)
            {
                a ^= x;
            }
            else
            {
                b ^= x;
            }
        }
        if (a > b)
        {
            std::swap(a, b);
        }
        return {a, b};
    }
};