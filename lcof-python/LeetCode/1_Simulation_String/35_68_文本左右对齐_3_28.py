def blank(n) -> int:
    return " " * n
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        right,n = 0,len(words)
        while True:
            # 当前行数的第一个
            left = right
            sumLen = 0
            # 判断每一行装多少个 每一个单词之间 要加空格 right== n 就是最后一个了
            while right < n and sumLen+len(words[right]) +right -left <= maxWidth:
                sumLen += len(words[right])
                # 贪心 right本身包含了单词之间至少有一个空格的计算
                right+=1
            # 最后一个 也是循环出口
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth- len(s)))
                break
            # 当前行的单词数
            numWords = right - left
            # 需要填充空格数
            numSpace = maxWidth- sumLen
            # 当前行只有一个单词：该单词左对齐，在行末填充空格
            if numWords == 1:
                ans.append(words[left] + blank(numSpace))
                continue
            avgSpace = numSpace // (numWords - 1)
            # 左边的需要填充的要大于右边 余数说明这么多个中间的需要extraSpace个额外的空格 也就是extraSpace+1个单词
            extraSpace = numSpace % (numWords -1)
            s = blank(avgSpace+1).join(words[ left : left + extraSpace + 1])
            s += blank(avgSpace)
            # 和上面右边保持一致
            s+= blank(avgSpace).join(words[left+extraSpace + 1:right])
            ans.append(s)

        return ans