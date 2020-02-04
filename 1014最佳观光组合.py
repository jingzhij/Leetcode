class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left=A[0]+0
        res=0
        for i in range(1,len(A)):
            res=max(res,left+A[i]-i)
            left=max(left,A[i]+i)
        return res
