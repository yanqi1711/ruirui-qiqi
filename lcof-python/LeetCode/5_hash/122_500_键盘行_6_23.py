class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        ans = []
        # 集合操作
        for i in words:
            x = i.lower()
            x = set(x)
            if x<=set1 or x<=set2 or x<=set3:
                ans.append(i)
        return ans