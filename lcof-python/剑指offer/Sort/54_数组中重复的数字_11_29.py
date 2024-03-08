class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        if len(numbers) == 1:
            return -1
        mp = set()
        for i in numbers:
            if i not in mp:
                mp.add(i)
            else:
                return i
        return -1