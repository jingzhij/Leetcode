思路：首先每个人分一半糖果，如果set中的数量大于一半糖果的数量，那么肯定有一个人能够分到n/2的不同种类
如果set数量小于一半糖果的数量，那么返回set的长度，相当于把所有种类的糖果都给一个人
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        tmp=len(set(candies)  
        return len(candies)//2 if tmp>=len(candies)//2 else tmp
