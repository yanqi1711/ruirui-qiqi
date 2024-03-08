"""
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。
现在给一串数字，返回有多少种可能的译码结果
"""
class Solution:
    def solve(self , nums: str) -> int:
        # 清除0
        if nums == '0':
            return 0
        # 清除10 和 20
        if nums == '10' or nums == '20':
            return 1
        n = len(nums)
        my_list1 = [str(i) for i in range(11,20)]
        my_list2 = [str(i) for i in range(21,27)]
        my_list1.extend(my_list2)
        print(my_list1)
        # 判断极端情况 100 200 3000
        for i in range(1, n):
            if nums[i] == '0':
                if nums[i-1]!='1' and nums[i-1] != '2':
                    return 0
        dp = [1 for j in range(n)]
        if nums[0:2] in my_list1:
            dp[1]=2
        print(dp)
        for i in range(2,n):
            if nums[i-1:i+1] in my_list1:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-1]