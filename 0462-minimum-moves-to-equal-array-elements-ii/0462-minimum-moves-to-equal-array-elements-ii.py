from collections import Counter
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        a = nums[(len(nums)-1)//2]
        for i in nums:
            count+=(abs(i-a))
        return count



            
