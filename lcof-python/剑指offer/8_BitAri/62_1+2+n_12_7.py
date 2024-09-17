class Solution:
    def __init__(self) -> None:
        self.sum = 0
    def Sum_Solution(self, n):
        try:
            assert n or 0
            self.Sum_Solution(n-1)
        except:
            pass
        self.sum += n
        return self.sum