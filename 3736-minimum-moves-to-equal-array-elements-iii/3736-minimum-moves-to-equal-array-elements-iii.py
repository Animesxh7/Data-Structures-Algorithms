class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        a = max(nums)
        for i in nums:
            count += (a-i)
        return count
            
            
        
        