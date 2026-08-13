class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        ans=0
        if len(prices)<=1:
            return 0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                ans+=prices[r]-prices[l]
            l+=1
        return ans    