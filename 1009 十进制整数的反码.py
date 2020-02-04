class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bi=bin(N)
        res=0
        for i in bi[2:]:
            if i=="1":
                res=res*2
            else:
                res=res*2+1
        return res
      
