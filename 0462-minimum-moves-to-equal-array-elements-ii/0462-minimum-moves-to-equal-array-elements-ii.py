from collections import Counter
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        low = 0
        high = len(nums)-1
        count = 0
        mid = (low + high)//2
        a = nums[mid]
        for i in nums:
            count+=(abs(i-a))
        return count



            
