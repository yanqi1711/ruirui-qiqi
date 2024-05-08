from typing import List


def getKth(nums1, start1, end1, nums2, start2, end2, k):
    len1 = end1 - start1 + 1
    len2 = end2 - start2 + 1
    # 因为是递归所以会一直交换 
    # 保证len1数组长度一定小于另一个
    if len1 > len2:
        return getKth(nums2, start2, end2,nums1,start1,end1,k)
    if len1 == 0:
        # 索引包含0 所以需要-1
        return nums2[start2 + k - 1]
    if k == 1:
        print(nums1[start1], nums2[start2])
        return min(nums1[start1], nums2[start2])
    # 神之一手 比较最小值 从而不需要考虑边界条件
    i = start1 + min(len1, k>>1) -1
    j = start2 + min(len2, k>>1) -1
    # 必须是大于不能有等于 不然就不能把nums1截断
    if nums1[i] > nums2[j]:
        # 1大于2 截断2 
        return getKth(nums1, start1, end1, nums2, j+1, end2 , k - (j - start2 + 1))
    # 
    else:
        return getKth(nums1, i+1, end1, nums2, start2, end2 , k - (i - start1 + 1))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        # 偶数就是找到这2个数
        left = (m+n+1) >>1
        right = (m+n+2) >> 1
        # 奇数 left == right 5 (5+1) // 2 = 3 (5+2) // 2 = 3
        if left == right:
            return getKth(nums1, 0, m-1, nums2, 0, n-1, left)
        # 偶数
        else:
            return (getKth(nums1, 0, m-1, nums2, 0, n-1, left)+getKth(nums1, 0, m-1, nums2, 0, n-1, right)) * 0.5
    


if __name__ == "__main__":
    s = Solution()
    nums1 = [3]
    nums2 = [1,2]
    print(s.findMedianSortedArrays(nums1,nums2))