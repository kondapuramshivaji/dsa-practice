class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        x=len(nums)//2
        y=nums[x]
        return y    
        