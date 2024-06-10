"""
给定一正整数数组 nums，nums 中的相邻整数将进行浮点除法。例如， [2,3,4] -> 2 / 3 / 4 。
例如，nums = [2,3,4]，我们将求表达式的值 "2/3/4"。
但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，以便计算后的表达式的值为最大值。
以字符串格式返回具有最大值的对应表达式。
注意：你的表达式不应该包含多余的括号
"""
# 别想太多 不是求 局部 最大值
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        length = len(nums)
        if length == 1:
            return str(nums[0])
        if length == 2:
            return str(nums[0]) + "/" + str(nums[1])
        # dp要n^3
        return  str(nums[0]) + "/(" + "/".join(map(str, nums[1:]))  +")"