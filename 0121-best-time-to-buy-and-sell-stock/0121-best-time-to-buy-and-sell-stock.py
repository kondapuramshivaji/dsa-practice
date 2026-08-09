class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        ans=0
        minval=prices[0]
        for i in range(1,l):
            ans=max(ans,prices[i]-minval)
            minval=min(minval,prices[i])
        return ans    