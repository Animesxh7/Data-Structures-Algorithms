class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        count = 1
        maxi = 1
        for i in range(len(nums)-1):
            if  nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                count+=1
            else:
                count = 1 
            maxi = max(maxi,count)
        return maxi


        