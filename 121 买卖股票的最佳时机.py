思路：
当前最大收益=max(前i-1天最大收益，今天价格 减去 前i-1天最小价格)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_value=prices[0]
        res=0
        for i in range(1,len(prices)):
            res=max(res,prices[i]-min_value)
            if prices[i]<min_value:
                min_value=prices[i]
        return res







