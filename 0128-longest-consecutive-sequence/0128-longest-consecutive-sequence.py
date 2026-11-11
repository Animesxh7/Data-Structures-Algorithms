class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        a = set(nums)
        maxi = 0
        for i in a:
            if  i+1 in a:
                continue
            count = 1
            while i-1 in a:
                i-=1
                count+=1 
            maxi = max(maxi,count)
        return maxi


        