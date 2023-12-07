class Solution:
    def NumberOf1(self , n: int) -> int:
        # 负数用补码表示，故不能用连除法
        # 这题有32位 必须固定
        # n & (n-1) 最低位会变为1
        count = 0
        for i in range(32):
            if n & (1<<i):
                count += 1
        return count