class Solution
{
public:
    void backtrack(vector<vector<int>> &res, vector<int> &output, int first, int len)
    {
        // 参数中output其实就是每一个得答案 因为函数递归他会保存自身得栈
        if (first == len) // 所有数都填完了 要把自身加入
        {
            res.emplace_back(output);
            return;
        }
        for (int i = first; i < len; ++i)
        {
            // 关键 更新已经使用数组
            // 如果是 [1,2,3]首次调用那么就不会swap 但是当i++的时候 此时 2就会和1交换 从而达到更换排列的目的
            swap(output[i], output[first]);
            // 继续递归填下一个数
            backtrack(res, output, first + 1, len);
            // 撤销操作
            swap(output[i], output[first]);
        }
    }
    vector<vector<int>> permute(vector<int> &nums)
    {
        vector<vector<int>> res;
        backtrack(res, nums, 0, nums.size());
        return res;
    }
};