两个转移方程dp[i][0]=max(dp[i-1][0],dp[i-1][1]+price[i])
          dp[i][1]=max(dp[i-1][1],dp[i-2][0]-price[i])
# dp_i_1表示第i天有股票，dp_i_0表示第i天无股票
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_1=float("-inf")
        dp_i_0=0
        dp_pre=0
        for i in range(len(prices)):
            temp=dp_i_0
            dp_i_0=max(dp_i_0,dp_i_1+prices[i])
            dp_i_1=max(dp_i_1,dp_pre-prices[i])
            dp_pre=temp
        return dp_i_0
