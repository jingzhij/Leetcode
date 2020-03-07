#思路： 首先确定好前两个数的循环范围，然后确定前两个数，放入递归判断是否满足条件，因为有“0”，所以麻烦了些
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        def helper(first,second,k):
            third=first+second
            if num.find(str(third),k)==k:
                if k+len(str(third))==n:
                    return True
                else:
                    return helper(second,third, k+len(str(third)))
            return False
        for i in range(1,n//2+1):
            for j in range(i+1,n//3*2+1):
                if int(num[i])==0 and len(num[i:j])!=1:
                    continue
                if int(num[0])==0 and len(num[:i])!=1:
                    continue
                if helper(int(num[:i]),int(num[i:j]),j):
                    return True
                else:
                    continue
        return False
    
