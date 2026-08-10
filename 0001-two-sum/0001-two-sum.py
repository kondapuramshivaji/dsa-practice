class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}  
        for i,num in enumerate(nums):
            dif=target-num
            if dif in d:
                return [d[dif],i]
            d[num]=i    
        