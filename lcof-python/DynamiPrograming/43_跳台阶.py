class Solution:
    def jumpFloor(self , number: int) -> int:
        if number == 1:
            return 1
        if number == 2:
            return 2
        # 超时 应该是爆栈
        # return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
        step1 = 1
        step2 = 2
        for i in range(3,number + 1):
            result = step1 + step2
            step1 = step2
            step2 = result
        return result