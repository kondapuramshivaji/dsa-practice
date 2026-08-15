class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        x=-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1]<nums[i]:
                x=i-1
                break
        if x!=-1:
            for j in range(len(nums)-1,x,-1):
                if nums[j]>nums[x]:
                    nums[j],nums[x]=nums[x],nums[j]
                    break
        l=x+1
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        return nums                        
        