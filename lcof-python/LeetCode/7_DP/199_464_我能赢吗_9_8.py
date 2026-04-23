class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 如果目标为0，当前玩家自动获胜
        if desiredTotal == 0:
            return True
        # 如果所有数字加起来都不足以达到目标，则当前玩家无法获胜
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        dp = dict()

        def dfs(state, total):
            # 已经遍历过这个结果
            if state in dp:
                return dp[state]
            # 遍历 找所有的结果 因为是最优 所以肯定要走完所有情况 并且自己一定赢
            for i in range(1, maxChoosableInteger+1):
                # 当前状态没有被选择
                if not (state & (1 << (i-1))):
                    # 需要找当前的使自己能赢的状态 所以不能把原来的覆盖 因为可能会取不同的情况
                    # (如选择3 或者5 他们每一个单独相加都是不一样的情况)
                    newTotal = total + i
                    # 更新状态 不能直接等于 直接赋值会覆盖之前的已经存在的状态
                    newState = state | (1 << (i-1)) # 从1开始的
                    # 非常关键 
                    # 1.先手无法满足total>=desiredTotal时 经过后面的dfs找到所有可能的情况 
                    #   当跑完所有的maxChoose时还是无法使得自己赢 返回False
                    # 2. 当进入后手时 也会找到所有使得自己赢得情况才会返回
                    if newTotal >= desiredTotal or not dfs(newState, newTotal):
                        dp[state] = True
                        return True
            # 记录旧状态即可 因为新得会进入递归循环里
            dp[state] = False
            return False
        # 找先手能赢得状态
        return dfs(0, 0)