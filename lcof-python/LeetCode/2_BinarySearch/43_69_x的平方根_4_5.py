class Solution:
    def mySqrt(self, x: int) -> int:
        maxValue = 46340
        if x < maxValue:
            maxValue = x
        left, right = 0, maxValue
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid*mid <= x:
                ans = mid
                print(ans , mid)
                left = mid + 1
            else: 
                right = mid - 1
        return ans