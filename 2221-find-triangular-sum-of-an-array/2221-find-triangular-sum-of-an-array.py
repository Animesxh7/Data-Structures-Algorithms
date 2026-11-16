class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums)>1:
            new = [0]*(len(nums)-1)
            for i in range(len(nums)-1):
                new[i] = (nums[i]+nums[i+1])%10
            nums = new
        return nums[0]
