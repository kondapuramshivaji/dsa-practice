class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l=0
        temp=1
        ans=0
        for r in range(len(nums)):
            temp*=nums[r]
            while temp>=k:
                temp//=nums[l]
                l+=1
            ans+=r-l+1
        return ans            