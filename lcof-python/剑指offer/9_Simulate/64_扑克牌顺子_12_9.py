class Solution:
    def IsContinuous(self , numbers: List[int]) -> bool:
        # write code here
        hash = set()
        for i in numbers:
            if i in hash:
                return False
            hash.add(i)
            if i == 0:
                hash.discard(0)
        min_value,max_value = min(hash), max(hash)
        if max_value - min_value >= 5:
            return False
        else:
            return True