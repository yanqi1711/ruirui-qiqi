class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int n = (int)nums.size();
        if (!n)
        {
            return -1;
        }
        if (n == 1)
        {
            return nums[0] == target ? 0 : -1;
        }
        int l = 0, r = n - 1;
        while (l <= r)
        {
            int mid = (l + r) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[0] <= nums[mid])
            {
                if (nums[0] <= target && target < nums[mid])
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            else
            {
                if (nums[mid] < target && target <= nums[n - 1]) // mid已经对比过了 所以不需要等于
                    l = mid + 1;
                else
                    r = mid - 1; // 回归到最开始得情况 部分有序，所以只需要控制范围即可
            }
        }
        return -1;
    }
};