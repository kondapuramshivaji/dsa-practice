class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        answer=nums[0]
        current_max=nums[0]
        current_min=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            a=x
            b=current_max*x
            c=current_min*x
            if a > b and a>c:
                newmax=a
            elif b>c:
                newmax=b
            else:
                newmax=c
            if a < b and a<c:
                newmin=a
            elif b<c:
                newmin=b
            else:
                newmin=c 
            current_max=newmax
            current_min=newmin
            if current_max> answer:
                answer=current_max
        return answer            















