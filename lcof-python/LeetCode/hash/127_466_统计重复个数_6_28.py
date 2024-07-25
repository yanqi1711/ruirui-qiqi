class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        # s2_cnt 代表s2 在s1中出现的次数
        index, s1_cnt, s2_cnt = 0,0,0
        indexdict = {}
        # 找循环节
        while True:
            s1_cnt += 1
            # 遍历一次s1 找最后匹配的index 每次记录这个index 重复了 就代表找到了
            for c in s1:
                if c == s2[index]:
                    index += 1
                    # 如果完整的找到一个s2(不一定是循环节， 可能s1把s2完整包含, 也有可能s2跨越了s1)， 重置
                    if index == len(s2):
                        s2_cnt += 1
                        index = 0
            # 如果遍历完了,说明循环没找到循环节 直接返回
            if s1_cnt == n1:
                return s2_cnt // n2
            # 找到循环节了
            if index in indexdict:
                s1_pre, s2_pre = indexdict[index]  # 获取之前的s1，s2个数
                pre_loop = (s1_pre, s2_pre) # 组合成元组 用来计算

                # 内部循环节 结构 即:多少个s1 包含多少个s2 最后数量就是 ((n1 - pre_loop[0])//in_loop[0])*in_loop[1]
                in_loop = (s1_cnt - s1_pre, s2_cnt-s2_pre)
                break
            else: # 没找到就存进去
                indexdict[index] = (s1_cnt, s2_cnt)
        
        # 获取当前多少个s2被匹配 所以是pre_loop[1] + 循环节中 s2数
        ans = pre_loop[1] + (n1 - pre_loop[0])//in_loop[0]*in_loop[1]
        # 获得最后余下循环节几部分 ,假设循环节是3个s1  1 最后剩下两个部分+开头不是循环节的部分
        # 例如: [1,(2,3,4] [1),(2,3,4] [1),2,3,4]
        rest = (n1 - pre_loop[0]) % in_loop[0]
        # 因为pre_loop保存的就是前面第一个无法组成循环节的部分信息
        for i in range(rest):
            # 遍历剩下所有的s1
            for c in s1:
                #  index保存了循环节的断点 和 preloop中的index是一样的
                if c == s2[index]:
                    index += 1
                    if index == len(s2):
                        ans += 1
                        index = 0
        return ans // n2
