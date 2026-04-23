#include <vector>
class Solution
{
private:
    int p{0};

public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型vector
     * @return int整型
     */
    void paritition(vector<int> &nums, int left, int right)
    {
        if (left >= right)
            return;
        int mid = left + (right - left) / 2;
        paritition(nums, left, mid);
        paritition(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }
    void merge(vector<int> &nums, int left, int mid, int right)
    {
        vector<int> temp(right - left + 1);
        int i = left, j = mid + 1, k = 0;
        while (i <= mid && j <= right)
        {
            if (nums[i] <= nums[j])
            {
                temp[k++] = nums[i++];
            }
            else
            {
                // 当 左边的大于右边的时候的时候 说明已经排序的
                temp[k++] = nums[j++];
                p = (p + (mid - i + 1)) % 1000000007;
            }
        }
        // 合并剩下的
        while (i <= mid)
        {
            temp[k++] = nums[i++];
        }
        while (j <= right)
        {
            temp[k++] = nums[j++];
        }
        // 将排序后的元素放回原数组
        for (int m = 0; m < temp.size(); m++)
        {
            nums[left + m] = temp[m];
        }
    }

    int InversePairs(vector<int> &nums)
    {
        p = 0;
        paritition(nums, 0, nums.size() - 1);
        return p;
    }
};