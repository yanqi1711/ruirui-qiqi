class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        n = len(nums)
        # k 就是k个桶 也就是数组的大小
        bucket = [0] * k
        target = sum(nums) / k
        if nums[0] > target: return False

        # 当前index 表示搜索到了nums的哪个数字
        def backtrace(index):
            # 全部塞进桶里面了 说明找到了 不装满会全部回溯
            # 例子: 10 10 2 2 k=2 target=12 => 0 [10] 1 [10]--> 0 [10, 2] 1 [10, 2] --> index+=1 = 4刚好装满
            if index == n: return True
            for i in range(k):
                # 重点优化
                # 剪枝
                # 把这个example: 10 10 1 3  k = 2 target=12 跑一遍就知道了
                # 因为上面在 0 [10] 1 [10]的时候对于0号bucket需要走一个选1 一个选3的路线但是结果是都回溯 
                # 如果没有这个优化 对于第二个桶还要再走一遍这个过程 并且这个会回溯到第一号桶装一开始0的情况
                # LFool的第三个优化说包含在这第二个优化里 就是这样的
                # for (int i = 0; i < k; i++) { #任意放到某个桶中的效果都是一样的，所以我们规定放到第一个桶中
                #     if (i > 0 && index == 0) break ;
                #     // 其他逻辑不变
                # 作者：LFool⚡
                # 链接：https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solutions/1441006/by-lfool-d9o7/
                if i>0 and bucket[i] == bucket[i-1]: continue
                # 开始装数字 大于就下一个桶子来装
                if bucket[i] + nums[index] > target: continue
                # 没有就装进去再说
                bucket[i] += nums[index]
                # 开始找index装入当前桶的其他情况是否符合
                if (backtrace(index+1)): return True
                # 不符合就回溯
                bucket[i] -= nums[index]
            # 所有情况找完了都没找到
            return False
        return backtrace(0)