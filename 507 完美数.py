class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        factor=[1]
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                factor.append(i)
                factor.append(num//i)
        print(factor)
        return sum(factor)==num
