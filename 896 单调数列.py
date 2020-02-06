class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        pos=False
        neg=False
        for i in range(len(A)-1):
            dif=A[i+1]-A[i]
            if dif>0:
                pos=True
            elif dif<0:
                neg=True
        return not (pos and neg)
