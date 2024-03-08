class Solution:
    def reOrderArray(self , array: List[int]) -> List[int]:
        if not array:
            return []
        res = []
        i = 0
        n = len(array)
        while i < n:
            if array[i] % 2 == 1:
                res.append(array[i])
                array.remove(array[i])
                n -= 1
            else:
                i += 1
        res.extend(array)
        return res