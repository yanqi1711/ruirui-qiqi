class Solution:
    def isHappy(self, n: int) -> bool:
        myset = set()
        def spiltNum(num):
            nonlocal myset
            if num in myset:
                return False
            myset.add(num)
            cur = 0
            while num:
                cur += (num % 10)**2
                num = num // 10
            if cur == 1:
                return True
            else:
                return spiltNum(cur)
        return spiltNum(n)