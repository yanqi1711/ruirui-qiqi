class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            n = 1
            while n:
                # 删除3个及以上的字符串 返回n用来捕获
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        # 第 1 个剪枝条件：手中颜色相同的球每次选择时只需要考虑其中一个即可
        hand = "".join(sorted(hand))
        # 三个元素分别为桌面球状态、手中球状态和回合数
        queue = deque([(board, hand, 0)])

        # 没有键值对 是set类型 维护的已访问过的状态
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            # 在第i的位置插入第j的颜色球 使用 product 生成 cur_board 和 cur_hand 的所有可能插入位置。
            for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
                # 第 1 个剪枝条件: 当前球的颜色和上一个球的颜色相同
                if j > 0 and cur_hand[j] == hand[j - 1]: #因为排序过了
                    continue
                # 第 2 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球
                # 新插入的球和插入位置左侧的球的颜色相同，则跳过这个位置
                if i > 0 and cur_board[i - 1] == cur_hand[j]: #
                    continue

                choose = False
                #  - 第 1 种情况 : 当前球颜色与后面的球的颜色相同 
                if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                    choose = True
                # 第2种 存在插入球与左右两边不一样的颜色 但是左右两边是一样的颜色
                #  RRWWRRBBRR，手中的球为 WB，答案为 2
                # RRWWRRBBRR → RRWWRRBBR(W)R[两边相同了] → RRWWRR(B)BBRWR[第一种情况] → RRWWRRRWR → RRWWWR → RRR → ""
                if 0< i < len(cur_board) and cur_board[i] == cur_board[i-1] and cur_hand[j]:
                    choose = True
                # 第三种 插入新球与插入位置两侧的球颜色均不相同，且插入位置两侧的球的颜色不同
                # 这种实际上和第一种一样 
                # WWRRBBWW → WWRRBB(R)WW → WWRRB(B)BRWW → WWRRRWW → WWWW →"" 桌面上的球为 WWRRBBWW，手中的球为 WWRB，答案为 2
                if choose:
                    # 在当前cur_board添加hand手中的颜色 然后进行清屏
                    new_board = clean(cur_board[:i] + cur_hand[j] + cur_board[i:])
                    new_hand = cur_hand[:j] + cur_hand[j + 1:]
                    if not new_board:
                        # 都清完了
                        return step + 1
                    if (new_board, new_hand) not in visited:
                        #  得到新状态加入 step+1表示进行了一次操作
                        queue.append((new_board, new_hand, step + 1))
                        visited.add((new_board, new_hand))
        return -1
