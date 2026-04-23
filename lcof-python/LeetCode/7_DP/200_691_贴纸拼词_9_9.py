# 找所有可能组合的情况
"""
stickers: [with, example, science] target: thehat
    全局最优肯定要找到所有情况 通过一下几种情况每次比较dp[-1]的最小值
    重点就是在于 每个单词匹配完 整个target后 需要从头(stickers)找到其余的不同情况进行匹配+比较
                         --           
第一次遍历找到2种   with(000011) ----> with(101011) -> example(111111)=>
                                ---->  example(000111) -> with(1111111)
                    example(010100) -->with(010111) -> with(111111)
"""

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        # n+1代表不可达到 因为如果存在 target最多每个字符由不同的单词组成
        dp = [n+1] * (1 << n)
        # 初始化初始状态 
        # 第一次肯定要尝试找到 部分字母在里面的情况
        # 当空的字符，需要的贴纸数量为0
        dp[0] = 0 # 含义:最少需要贴纸数量
        # 尝试找到所有情况 寻找最优值 如果到最后还没把dp[(1<<n)-1]重置说明没有解
        for bit in range(1 << n):
            # 第一次都没找到在单词里找到target的字母 会一直continue
            # 找所有可能组合的情况
            if dp[bit] == (n+1):
                continue
            # 每一个状态都要找stickers里面的所有单词找到所有匹配情况
            for word in stickers:
                # state用来更新每次找到stickers里存在target部分情况，对应最上面 需要找到不同的情况比较
                state = bit
                for c in word:
                    for i in range(n):
                        # 如果字母一样 并且没有被占用
                        if target[i] == c and ((state >> i) & 1) == 0:
                            # 更新状态
                            state = state | (1 << i)
                            # target中的字母匹配完了 需要找下一个
                            break
                # 每一个word 找完了都需要更新比较状态 找到最小值 每一个单词匹配先后顺序不同 结果不同
                # 换一个案例 [withea example] target: thehat 最小只需要2个 但是顺序也可以  example->withea-<withea =>3次
                # dp[bit] 就是当前已经操作的次数
                dp[state] = min(dp[state], dp[bit] + 1)
        return dp[-1] if dp[-1] != (n+1) else -1