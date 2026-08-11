class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        temp = 0
        ans = 0
        dici = {}
        for r in range(len(nums)):
            dici[nums[r]] = dici.get(nums[r], 0) + 1
            temp += nums[r]
            if r - l + 1 > k:
                dici[nums[l]] -= 1
                temp -= nums[l]
                if dici[nums[l]] == 0:
                    dici.pop(nums[l])
                l += 1
            if r - l + 1 == k and len(dici) == k:
                ans = max(ans, temp)
        return ans