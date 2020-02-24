思路：动态规划，dp[i]=min(dp[i],dp[i-coin]),当前的数量等于 当前数量和当前数量减去相应coin 中的最小值，自底向上
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]!=float("inf") else -1
        

