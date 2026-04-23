from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        缝隙 = dict()
        for i in wall:
            cur = 0
            # 最后的边界不能要
            for j in i[:-1]:
                cur += j
                # 每一个都是一个缝隙 需要保存起来
                缝隙[cur] = 缝隙.get(cur, 0) + 1
        # 找到缝隙最多的点
        max_ = 0
        for value in 缝隙.values():
            max_ = max(max_, value)
        return len(wall) - max_