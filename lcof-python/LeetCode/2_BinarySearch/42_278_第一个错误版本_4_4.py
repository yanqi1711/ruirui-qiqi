# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            mid = (left +right) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid +1
        return left
