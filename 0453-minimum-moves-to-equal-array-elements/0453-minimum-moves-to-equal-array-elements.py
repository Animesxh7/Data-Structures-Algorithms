class Solution:
    def minMoves(self, nums: list[int]) -> int:
        a = min(nums)
        count = 0
        for i in nums:
            if i!=a:
                count+=(i-a)
        return count
