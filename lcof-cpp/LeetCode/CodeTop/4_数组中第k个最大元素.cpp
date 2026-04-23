class Solution
{
public:
    void adjust_heap(vector<int> &nums, int root)
    {
        // 最小堆 最小的在上面 最大的在下面
        int child = 2 * root + 1;
        // 保证已堆化情况下 当前root结点一定是最小的
        while (root < nums.size())
        {
            // 右孩子存在 并且更小
            if (child + 1 < nums.size() && nums[child] > nums[child + 1])
                ++child; // 调整到右子树 (在初始化堆的时候就已经满足堆的性质 所以只需要找到左右最小的 然后递归向下就可以了)
            if (child < nums.size() && nums[root] > nums[child])
                std::swap(nums[root], nums[child]);
            root = child;
            child = 2 * child + 1;
        }
        return;
    }

    int findKthLargest(vector<int> &nums, int k)
    {
        if (k > nums.size())
            return *std::max_element(nums.begin(), nums.end());
        vector<int> heap; // k个最小堆
        heap.reserve(k);
        for (int i = 0; i < k; ++i)
            heap.emplace_back(nums[i]); // 先初始化
        std::cout << heap.size() << std::endl;
        for (int j = k / 2; j > -1; --j)
            adjust_heap(heap, j);
        for (int i = k; i < nums.size(); ++i)
        {
            if (nums[i] < heap[0])
                continue;
            heap[0] = nums[i];
            adjust_heap(heap, 0);
        }
        return heap[0];
    }
};