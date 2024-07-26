class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = {}
        # 统计每一个词的频率
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        ans = 0
        # 查找相差1的
        for key,value in frequency.items():
            # 只需要检查+1或者-1因为每一个都会被遍历到 所以只要一个
            # 如果同时存在 [1,2,3]不合题意 而 1 2 2 2自己时一对 2,2,2,3,3时另外一队 遍历的时候直接全部包括了
            if key+1 in frequency:
                ans = max(ans, value + frequency[key+1])
        return ans