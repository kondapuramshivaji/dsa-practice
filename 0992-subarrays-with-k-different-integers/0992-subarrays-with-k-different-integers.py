class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def check(nums,k):
            l=0
            d={}
            ans=0
            for r in range(len(nums)):
                d[nums[r]]=d.get(nums[r],0)+1
                while len(d)>k:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        d.pop(nums[l])
                    l+=1
                ans+=r-l+1
            return ans  
        return check(nums,k)-check(nums,k-1)        