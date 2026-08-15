class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans=1
        long=1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
    
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                ans+=1
            else:
                ans=1
            long=max(long,ans)    

        return long        

                   