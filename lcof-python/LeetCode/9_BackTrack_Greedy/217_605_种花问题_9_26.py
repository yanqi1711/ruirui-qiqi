class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False
        # 遍历每一个位置，尝试种花
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:  # 当前格子为空
                # 检查前后格子是否满足条件：前后都没有花或者是边界
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1  # 种花
                    n -= 1  # 需要种的花减少1
                    if n == 0:  # 如果已经种完所有的花，返回True
                        return True
        
        return n <= 0 