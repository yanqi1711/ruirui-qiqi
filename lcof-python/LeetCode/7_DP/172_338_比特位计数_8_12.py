from typing import List


class Solution:
    # 求 [0,n] 中间的所有数的二进制1的个数
    def countBits(self, n: int) -> List[int]:
        if n < 0:
            return []
        ans = [0]
        flag = 1
        for i in range(1,n+1):
            if flag:
                ans.append(1+ans[i//2])
                flag ^= 1
            else:
                ans.append(ans[i//2])
                flag ^= 1
        return ans