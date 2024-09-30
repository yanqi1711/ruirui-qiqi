class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right = 0, len(citations) - 1
        n = right + 1
        while left <=  right:
            mid = (left + right) >> 1
            # citations[mid]表示 引用次数 
            # length - mid 代表有length - mid篇论文
            # 引用次数 >= 论文数
            if citations[mid] >=  n - mid:
                right = mid - 1
            else:
                left = mid +1
        return n-left