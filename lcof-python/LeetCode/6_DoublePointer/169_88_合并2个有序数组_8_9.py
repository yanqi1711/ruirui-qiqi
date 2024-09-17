from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 类似归并排序 比nums小 就continue 比nums大 就交换位置
        # 重点 后面有空位 从后面开始归并
        if not nums2:
            return nums1
        p1,p2 = m-1,n-1
        tail = m+n-1
        while p1 >= 0 and p2>= 0:
            if nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1-=1
            else:
                nums1[tail] = nums2[p2]
                p2-=1
            tail -= 1
        while p1 >= 0:
            nums1[tail] = nums1[p1]
            p1 -= 1
            tail -= 1
        while p2 >= 0:
            nums1[tail] = nums2[p2]
            p2 -= 1
            tail -= 1
        