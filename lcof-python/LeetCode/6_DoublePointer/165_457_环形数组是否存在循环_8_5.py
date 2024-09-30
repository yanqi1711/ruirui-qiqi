from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)

        def next(cur):
            # 循环
            return (cur + nums[cur]) % n
        
        # 开始循环 跑到数组长度n时 还没找到 肯定返回True了
        for i,num in enumerate(nums):
            # 排除已经遍历过的元素 因为不为环的话 已经遍历过的 一定不是环 是环的话已经跳出
            if num == 0: #本身为0 没用 直接
                continue
            slow = i
            fast = next(i)
            # 排除 一正一负的情况
            # 必须是nums[slow] 因为循环中 slow 会变化 直接写本次的num就无意义
            # fast每次要跳两次
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next(fast)] > 0:
                if slow == fast:
                    if slow == next(slow):
                        break
                    return True
                slow = next(slow)
                fast = next(next(fast))
            
            add = i
            # 把已经经过的地点 变为0 让后续的循环 跳过已经经过的路径
            while nums[add] * nums[next(add)] > 0: # 也要保证同号 之前的快慢指针可能就是一正一负跳出 所以也需要标记
                temp = add
                add = next(add)
                nums[temp] = 0
        # 循环完了 都没找到
        return False