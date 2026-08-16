class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        d={0:1} 
        ans=0
        for num in nums:
            prefix+=num
            target=prefix-k
            if target in d:
                ans+=d[target]
            d[prefix]=d.get(prefix,0)+1 
        return ans       
