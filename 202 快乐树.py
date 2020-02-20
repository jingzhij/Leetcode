题解: 把出现过的数字记录在集合里面

class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        n=str(n)    
        while True:
            n= str(sum(int(i)**2 for i in n))
            if n=="1":
                return True
            if n in visited:
                return False
            visited.add(n)
