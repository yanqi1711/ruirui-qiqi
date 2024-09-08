class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
        currentSum = maxSum = sum(nums[0 : k])
        for i in range(k, len(nums)):
            currentSum = currentSum + nums[i] - nums[i - k]
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum / k
