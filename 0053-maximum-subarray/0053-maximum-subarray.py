class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float('-inf')
        sumi = 0
        for i in range(len(nums)):
            sumi+=nums[i]
            maxi = max(maxi,sumi)
            if sumi<0:
                sumi = 0
        return maxi