思路：前缀树 

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res=0
        mask=0
        for i in range(31,-1,-1):
            mask|=(1<<i)
            s=set()
            for num in nums:
                s.add(num&mask)
            temp=res|(1<<i)
            for prefix in s:
                if prefix^temp in s:
                    res=temp
                    break
        return res
