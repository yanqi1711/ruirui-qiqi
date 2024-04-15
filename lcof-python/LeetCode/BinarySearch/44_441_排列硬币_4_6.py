class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        maxValue = 2147483647
        if n < maxValue:
            maxValue = n
        left, right = 0, maxValue
        ans = 0
        while left <= right:
            mid = (left + right ) // 2
            if ((mid * (mid - 1) // 2) <= n):
                ans = mid
                left = mid +1
            else:
                right = mid -1
        return ans -1