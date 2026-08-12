class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        temp=0
        l=0
        ans=0
        for r in range(len(nums)):
            if nums[r]==0:
                temp+=1
            while temp>k:
                if nums[l]==0:
                    temp-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans  