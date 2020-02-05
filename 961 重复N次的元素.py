class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashset=set()
        for i in A:
            if i in hashset:
                return i
            else:
                hashset.add(i)
                
