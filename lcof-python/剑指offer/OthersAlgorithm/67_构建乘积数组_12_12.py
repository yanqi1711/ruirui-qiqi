class Solution:
    def multiply(self , A: List[int]) -> List[int]:
        # 左右相乘 
        #    a0 a1 a2 a3 
        # b0 1  (a1 a2 a3)
        # b1 a0 1  (a2 a3)
        # b2 (a0 a1) 1  a3
        # b3 (a0 a1 a2) 1 
        length = len(A)
        B = [1 for i in range(length)]
        temp = 1
        for i in range(length):
            B[i] *= temp
            temp *= A[i]
        temp = 1
        for j in range(length-1,-1,-1):
            B[j] *= temp
            temp *= A[j]
        return B