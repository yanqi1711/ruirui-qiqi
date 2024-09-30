class Solution:
    def maxInWindows(self , num: List[int], size: int) -> List[int]:
        # write code here
        res = []
        #窗口大于数组长度的时候，返回空
        if size <= len(num) and size != 0:
            from collections import deque
            #双向队列
            # 保证左边pop的时候一定当前滑动窗口最大值
            dq = deque()
            # 先找到第一个窗口 之后再开始滑动
            for i in range(size):
                # 判断之前的数字是否大于当前数 不大于的数字全部删除
                while len(dq) != 0 and num[dq[-1]] < num[i]:
                    dq.pop()
                # 添加索引 可以使用索引判断是否滑向下一个窗口
                # 没有的话旧的使用count计数
                dq.append(i)
            for i in range(size, len(num)):
                # 第一个元素就是当前窗口最大值
                res.append(num[dq[0]])
                # 剔除第一个元素(dq[0]) 
                # 此时已经滑向下一个窗口 而最大值是最左边元素
                while len(dq) != 0 and dq[0] < (i - size + 1):
                    dq.popleft()
                while len(dq) != 0 and num[dq[-1]] < num[i]:
                    dq.pop()
                dq.append(i)
            res.append(num[dq[0]])
        return res


        # 2次循环
        # if len(num) < size or size == 0:
        #     return []
        # from collections import deque
        # dq = deque()
        # length = len(num) - (size -1)
        # res = []
        # for i in range(length):
        #     temp = num[i:i + size]
        #     res.append(max(temp))
        # return res