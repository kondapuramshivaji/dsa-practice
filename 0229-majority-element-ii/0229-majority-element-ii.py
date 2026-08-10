class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dici={}
        arr=[]
        for num in nums:
            dici[num]=dici.get(num,0)+1
        for num in dici:
            if dici[num] > len(nums)//3:
                arr.append(num)
        return arr        