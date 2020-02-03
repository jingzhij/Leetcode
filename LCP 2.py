class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        denominator=1               #分母
        numerator=cont[-1]          #分子
        n=len(cont)                 #长度
        for i in range(n-2,-1,-1):  #因为前面分子用到了最后一个，所以从n-2开始迭代
            denominator,numerator=numerator,denominator #交换分子分母
            numerator=cont[i]*denominator+numerator     #分母不变，分子通分
        return [numerator,denominator]
