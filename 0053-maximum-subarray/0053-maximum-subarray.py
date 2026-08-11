class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            if current+nums[i]>nums[i]:
                current=current+nums[i]
            else:
                current=nums[i]
            if current>max_sum:
                max_sum=current 
        return max_sum               