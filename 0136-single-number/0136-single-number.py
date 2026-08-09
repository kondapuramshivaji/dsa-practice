class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dici = {}

        for num in nums:
            dici[num] = dici.get(num, 0) + 1

        for key in dici:
            if dici[key] == 1:
                return key