class Solution:
    def printNumbers(self , n: int) -> List[int]:
        m = 1
        while(n):
            m *=10
            n-=1
        return [i for i in range(1, m)]